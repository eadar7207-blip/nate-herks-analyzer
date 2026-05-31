#!/usr/bin/env python3
"""
Nate Herks Video Analyzer - Extracts key insights from daily videos
Monitors YouTube feed, analyzes transcripts, and emails detailed summaries
"""

import feedparser
import os
import re
import json
import glob
import subprocess
from datetime import datetime, timedelta
from anthropic import Anthropic
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import time

# Initialize Anthropic client
client = Anthropic()

# YouTube RSS feed for Nate Herks (channel ID: UCLe7uWzLqitwx5Xc8vfvJvQ)
YOUTUBE_RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UCLe7uWzLqitwx5Xc8vfvJvQ"
CACHE_FILE = Path(__file__).parent / ".processed_videos.json"


def load_processed_videos():
    """Load list of already processed video IDs"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE) as f:
            return json.load(f)
    return []


def save_processed_videos(video_ids):
    """Save processed video IDs to cache"""
    with open(CACHE_FILE, "w") as f:
        json.dump(video_ids, f)


def get_youtube_feed():
    """Fetch latest videos from Nate Herks YouTube channel"""
    feed = feedparser.parse(YOUTUBE_RSS_URL)
    return feed.entries


def get_video_transcript(video_url):
    """Get transcript from YouTube video using yt-dlp and available subtitles"""
    sub_files = []
    try:
        subprocess.run(
            ["yt-dlp", "--write-auto-subs", "--sub-format", "vtt",
             "--skip-download", "-o", "temp", video_url],
            capture_output=True,
            text=True,
            timeout=60
        )

        sub_files = glob.glob("temp*.vtt")
        if sub_files:
            with open(sub_files[0]) as f:
                content = f.read()
            raw = [line.strip() for line in content.split('\n')
                   if line.strip() and not line.startswith('WEBVTT')
                   and '-->' not in line and not line[0].isdigit()]
            if not raw:
                return None
            deduped = [raw[0]] + [l for i, l in enumerate(raw[1:], 1) if l != raw[i-1]]
            return ' '.join(deduped)[:8000]
    except Exception as e:
        print(f"Failed to get transcript: {e}")
    finally:
        for f in sub_files:
            try:
                os.remove(f)
            except OSError:
                pass

    return None


def analyze_video_with_claude(video_title, transcript, video_url):
    """Use Claude to analyze video content for AI real estate insights"""

    if not transcript:
        return None

    analysis_prompt = f"""Analyze this Nate Herk video transcript and write exactly 4 paragraphs — no headers, no bullets, no markdown. Write in plain, simple language as if explaining to a smart friend who isn't deep in tech or AI. Avoid jargon; if you must use a term, explain it in the same sentence.

Paragraph 1: What the video is about and the core idea, in plain English.
Paragraph 2: The key method or framework introduced — what it is and why it works, simply explained.
Paragraph 3: How this applies to an AI real estate consulting business, with a concrete real-world example.
Paragraph 4: The single most actionable thing to do this week (specific and simple), plus one memorable quote from the video.

Video Title: {video_title}
Video URL: {video_url}

Transcript:
{transcript}"""

    try:
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=800,
            messages=[
                {"role": "user", "content": analysis_prompt}
            ]
        )
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

        # Attach HTML version
        msg.attach(MIMEText(html_content, "html"))

        # Send via Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
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
                <h2><a href="{video['url']}" target="_blank">{video['title']}</a></h2>
                <p style="font-size: 12px; color: #999;">Published: {video['published']}</p>
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
    paragraphs = [p.strip() for p in analysis_text.split('\n\n') if p.strip()]
    return ''.join(f"<p>{p}</p>" for p in paragraphs)


def save_latest_analysis(analyzed_videos):
    """Write plain-text analysis to latest_analysis.md so Claude Code can read it from the repo."""
    date_str = datetime.now().strftime("%B %d, %Y")
    lines = [f"# Nate Herk Analysis — {date_str}\n"]
    for v in analyzed_videos:
        # Strip HTML tags for plain markdown
        plain = re.sub(r'<[^>]+>', '', v['analysis']).strip()
        lines.append(f"## [{v['title']}]({v['url']})")
        lines.append(f"*{v['published']}*\n")
        lines.append(plain)
        lines.append("")
    output_path = Path(__file__).parent / "latest_analysis.md"
    output_path.write_text('\n'.join(lines))
    print("📄 Saved latest_analysis.md")


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

    # 48h window so caption-generation delays don't cause videos to be missed
    cutoff_time = datetime.now() - timedelta(days=2)

    for entry in entries[:5]:  # Check last 5 videos
        try:
            video_id = entry.id.split('yt:video:')[1]
            published = datetime(*entry.published_parsed[:6])
        except (IndexError, TypeError, AttributeError):
            print(f"⚠️  Skipping malformed feed entry: {getattr(entry, 'id', 'unknown')}")
            continue

        if video_id not in processed_videos:
            if published > cutoff_time:
                new_videos.append({
                    'id': video_id,
                    'title': entry.title,
                    'url': entry.link,
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
        transcript = get_video_transcript(entry.link)

        if transcript:
            # Analyze with Claude
            analysis = analyze_video_with_claude(
                video_info['title'],
                transcript,
                video_info['url']
            )

            if analysis:
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
