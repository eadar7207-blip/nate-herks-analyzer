#!/usr/bin/env python3
"""
Nate Herks Video Analyzer - Extracts key insights from daily videos
Monitors YouTube feed, analyzes transcripts, and emails detailed summaries
"""

import os
import re
import json
import subprocess
from datetime import datetime, timedelta
from html import escape
from anthropic import Anthropic
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import time

# Initialize Anthropic client
client = Anthropic()

CHANNEL_URL = "https://www.youtube.com/@nateherk/videos"
CACHE_FILE = Path(__file__).parent / ".processed_videos.json"


def load_processed_videos():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE) as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            print("⚠️  Cache file has unexpected format, starting fresh")
        except (json.JSONDecodeError, OSError):
            print("⚠️  Cache file corrupt, starting fresh")
    return []


def save_processed_videos(video_ids):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(video_ids, f)
    except OSError as e:
        print(f"⚠️  Could not save processed videos cache: {e}")


class _Entry:
    """Minimal feedparser-compatible entry parsed from YouTube Atom XML."""
    def __init__(self, id_, title, link, published_parsed):
        self.id = id_
        self.title = title
        self.link = link
        self.published_parsed = published_parsed


def get_youtube_feed():
    """Get latest videos from YouTube channel using yt-dlp."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--dump-json", "--playlist-end", "15", CHANNEL_URL],
            capture_output=True, text=True, timeout=120
        )
        entries = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                video_id = data.get('id', '')
                if not video_id:
                    continue
                title = data.get('title', '') or ''
                url = data.get('webpage_url') or f"https://www.youtube.com/watch?v={video_id}"
                upload_date = data.get('upload_date', '')
                if upload_date and len(upload_date) == 8:
                    pub_dt = datetime.strptime(upload_date, '%Y%m%d')
                else:
                    pub_dt = datetime.utcnow()
                entries.append(_Entry(f'yt:video:{video_id}', title, url, pub_dt.timetuple()))
            except Exception:
                continue
        if not entries and result.stderr:
            print(f"⚠️  yt-dlp returned no entries. stderr: {result.stderr[:300]}")
        return entries
    except Exception as e:
        print(f"⚠️  Feed fetch failed: {e}")
        return []


def get_video_transcript(video_url):
    """Get transcript using youtube-transcript-api v1.0+ (InnerTube API)."""
    from youtube_transcript_api import YouTubeTranscriptApi

    video_id_match = re.search(r'(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})', video_url)
    if not video_id_match:
        print(f"⚠️  Could not extract video ID from {video_url}")
        return None
    video_id = video_id_match.group(1)

    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id, languages=['en'])
        text = ' '.join(snippet.text for snippet in transcript)
        deduped = re.sub(r'(\b\S+\b)( \1\b)+', r'\1', text)
        print(f"   ✅ Got transcript ({len(deduped)} chars)")
        return deduped[:8000]
    except Exception as e:
        print(f"⚠️  Transcript fetch failed for {video_url}: {e}")
        return None


def analyze_video_with_claude(video_title, transcript, video_url):
    """Use Claude to analyze video content for AI real estate insights"""

    if not transcript:
        return None

    analysis_prompt = f"""Analyze this Nate Herk video transcript and write a full summary. Use plain, simple words — explain everything as if talking to a smart friend who isn't deep in tech or AI. If you use a technical term, explain it in the same sentence. No jargon left unexplained.

Structure your response exactly like this:

WHAT IT'S ABOUT
One short paragraph covering the main idea and why Nate made this video.

THE KEY POINTS
A bullet for each important point from the video. Keep each bullet short and clear. Bold the most critical insight on each bullet so it stands out.

THE METHOD OR FRAMEWORK
If Nate introduces a system, process, or way of doing something, explain it step by step in plain English. If there's no framework, skip this section.

HOW THIS APPLIES TO AI REAL ESTATE
A paragraph explaining how this directly applies to an AI real estate consulting business. Give a concrete example — a real scenario, not a vague idea.

ACTION STEP THIS WEEK
One specific thing to do this week. Not "explore" or "consider" — an actual action with clear steps.

BEST QUOTE
The single most memorable or useful line from the video, in quotation marks.

Video Title: {video_title}
Video URL: {video_url}

Transcript:
{transcript}"""

    try:
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": analysis_prompt}
            ]
        )
        if message.stop_reason == "max_tokens":
            print("⚠️  Analysis was truncated by max_tokens limit")
        if not message.content:
            print("❌ Claude returned empty content")
            return None
        return message.content[0].text
    except Exception as e:
        print(f"❌ Claude API error: {e}")
        return None


def send_email(recipient, subject, html_content):
    """Send email with analysis"""

    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("⚠️  EMAIL_SENDER or EMAIL_PASSWORD not set - skipping email")
        print("📧 Analysis would be sent to:", recipient)
        return False

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        msg.attach(MIMEText(html_content, "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())

        print(f"✅ Email sent to {recipient}")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False


def format_email_html(videos_analysis):
    """Format analysis results as HTML email"""

    date_str = datetime.now().strftime("%B %d, %Y")

    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 5px 0 0 0; opacity: 0.9; }}
            .video {{ margin-bottom: 40px; border-left: 4px solid #667eea; padding-left: 20px; }}
            .video h2 {{ margin-top: 0; color: #667eea; font-size: 18px; }}
            .video a {{ color: #667eea; text-decoration: none; }}
            .video a:hover {{ text-decoration: underline; }}
            .section {{ margin: 15px 0; }}
            .section-title {{ font-weight: 600; color: #333; margin-bottom: 8px; }}
            .highlight {{ background: #f0f4ff; padding: 12px; border-radius: 4px; margin: 10px 0; font-style: italic; color: #555; }}
            .insight {{ background: #f9f9f9; padding: 12px; border-radius: 4px; margin: 8px 0; }}
            .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #999; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎬 Nate Herks Daily Analysis</h1>
                <p>{date_str}</p>
            </div>
    """

    if not videos_analysis:
        html += "<p>No new videos analyzed today.</p>"
    else:
        for video in videos_analysis:
            html += f"""
            <div class="video">
                <h2><a href="{escape(video['url'])}" target="_blank">{escape(video['title'])}</a></h2>
                <p style="font-size: 12px; color: #999;">Published: {escape(video['published'])}</p>
                {video['analysis']}
            </div>
            """

    html += """
            <div class="footer">
                <p>This email is automatically generated daily by your Nate Herks Video Analyzer.</p>
                <p>Powered by Claude AI</p>
            </div>
        </div>
    </body>
    </html>
    """

    return html


def format_analysis_as_html(analysis_text):
    if not analysis_text:
        return "<p>Analysis unavailable.</p>"
    html_parts = []
    in_list = False
    for line in analysis_text.split('\n'):
        s = line.strip()
        if not s:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            continue
        if s.isupper():
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(f'<h3 style="color:#667eea;margin-top:18px;margin-bottom:4px;">{escape(s)}</h3>')
        elif s.startswith('- ') or s.startswith('• '):
            if not in_list:
                html_parts.append('<ul style="margin:6px 0;padding-left:20px;">')
                in_list = True
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(s[2:]))
            html_parts.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(s))
            html_parts.append(f'<p style="margin:6px 0;">{content}</p>')
    if in_list:
        html_parts.append('</ul>')
    return '\n'.join(html_parts)


def save_latest_analysis(analyzed_videos):
    date_str = datetime.now().strftime("%B %d, %Y")
    lines = [f"# Nate Herk Analysis — {date_str}\n"]
    for v in analyzed_videos:
        plain = v['raw_analysis'].strip()
        safe_title = v['title'].replace('[', '\\[').replace(']', '\\]')
        lines.append(f"## [{safe_title}]({v['url']})")
        lines.append(f"*{v['published']}*\n")
        lines.append(plain)
        lines.append("")
    try:
        output_path = Path(__file__).parent / "latest_analysis.md"
        output_path.write_text('\n'.join(lines), encoding="utf-8")
        print("📄 Saved latest_analysis.md")
    except OSError as e:
        print(f"⚠️  Could not save latest_analysis.md: {e}")


def main():
    """Main execution"""

    print("🎬 Nate Herks Video Analyzer Started")
    print(f"⏰ Time: {datetime.now().isoformat()}")

    # Load processed videos
    processed_videos = load_processed_videos()

    # Get latest videos
    entries = get_youtube_feed()
    print(f"📺 Found {len(entries)} recent videos in feed")

    new_videos = []
    videos_to_analyze = []

    # 7-day window; cache-based deduplication prevents re-processing
    cutoff_time = datetime.utcnow() - timedelta(days=7)

    for entry in entries[:5]:  # Check last 5 videos
        try:
            raw_id = entry.id.split('yt:video:')
            video_id = raw_id[1] if len(raw_id) > 1 else None
            if not video_id:
                print(f"⚠️  Skipping entry with empty video ID: {getattr(entry, 'id', 'unknown')}")
                continue
            title = entry.title
            link = entry.link
            published = datetime(*entry.published_parsed[:6])
        except (IndexError, TypeError, AttributeError):
            print(f"⚠️  Skipping malformed feed entry: {getattr(entry, 'id', 'unknown')}")
            continue

        if video_id not in processed_videos:
            if published > cutoff_time:
                new_videos.append({
                    'id': video_id,
                    'title': title,
                    'url': link,
                    'published': published.strftime("%B %d at %I:%M %p")
                })
                videos_to_analyze.append(entry)

    if not new_videos:
        print("✨ No new videos to analyze")
        return

    print(f"📹 Found {len(new_videos)} new video(s)")

    # Analyze each video
    analyzed_videos = []
    for entry, video_info in zip(videos_to_analyze, new_videos):
        print(f"\n🔍 Analyzing: {video_info['title'][:50]}...")

        # Get transcript
        transcript = get_video_transcript(video_info['url'])

        if transcript:
            # Analyze with Claude
            analysis = analyze_video_with_claude(
                video_info['title'],
                transcript,
                video_info['url']
            )

            if analysis:
                video_info['raw_analysis'] = analysis
                video_info['analysis'] = format_analysis_as_html(analysis)
                analyzed_videos.append(video_info)
                print("✅ Analysis complete")
                time.sleep(1)  # Rate limiting
            else:
                print("⚠️  Analysis failed")
        else:
            print("⚠️  Could not get transcript")

    if analyzed_videos:
        # Send email
        recipient = os.getenv("EMAIL_RECIPIENT", "eadar7207@gmail.com")
        subject = f"🎬 Nate Herks Daily Analysis - {len(analyzed_videos)} Video(s)"
        html_content = format_email_html(analyzed_videos)

        send_email(recipient, subject, html_content)

        # Save plain-text analysis to repo so it can be read from Claude Code
        save_latest_analysis(analyzed_videos)

        # Update processed videos
        new_processed = processed_videos + [v['id'] for v in analyzed_videos]
        save_processed_videos(new_processed)

        print(f"\n✅ Processing complete - {len(analyzed_videos)} video(s) analyzed")
    else:
        print("⚠️  No videos were successfully analyzed")


if __name__ == "__main__":
    main()
