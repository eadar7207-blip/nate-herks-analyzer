#!/usr/bin/env python3
"""
Nate Herks Video Analyzer - Extracts key insights from daily videos
Monitors YouTube feed, analyzes transcripts, and emails detailed summaries
"""

import os
import re
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html import escape
from anthropic import Anthropic
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import time

# Initialize Anthropic client
client = Anthropic()

CHANNEL_ID = "UC2ojq-nuP8ceeHqiroeKhBA"  # @nateherk
RSS_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
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


def _get_feed_via_ytdlp():
    """Fallback: use yt-dlp to list recent channel videos when RSS is blocked."""
    import subprocess
    import tempfile

    channel_url = f"https://www.youtube.com/@nateherk/videos"
    cookies_content = os.getenv("YOUTUBE_COOKIES")
    cookies_path = None
    entries = []

    try:
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "--playlist-end", "10",
            "--print", "%(id)s\t%(title)s\t%(upload_date>%Y-%m-%dT%H:%M:%S)s",
            "--no-warnings",
            "--quiet",
        ]
        if cookies_content:
            tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
            tmp.write(cookies_content)
            tmp.close()
            cookies_path = tmp.name
            cmd += ["--cookies", cookies_path]
        cmd.append(channel_url)

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"⚠️  yt-dlp exit {result.returncode}: {result.stderr[:200]}")
            return []

        for line in result.stdout.strip().splitlines():
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            video_id = parts[0].strip()
            title = parts[1].strip() if len(parts) > 1 else ''
            date_str = parts[2].strip() if len(parts) > 2 else ''
            try:
                pub_dt = datetime.fromisoformat(date_str) if date_str and date_str != 'NA' else datetime.now()
            except ValueError:
                pub_dt = datetime.now()
            link = f"https://www.youtube.com/watch?v={video_id}"
            entries.append(_Entry(f'yt:video:{video_id}', title, link, pub_dt.timetuple()))

        print(f"   ✅ yt-dlp returned {len(entries)} entries")
        return entries
    except Exception as e:
        print(f"⚠️  yt-dlp fallback failed: {e}")
        return []
    finally:
        if cookies_path:
            try:
                os.unlink(cookies_path)
            except OSError:
                pass


def get_youtube_feed():
    """Get latest videos from YouTube channel RSS feed, falling back to yt-dlp."""
    import http.cookiejar
    import tempfile

    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'yt': 'http://www.youtube.com/xml/schemas/2015',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/atom+xml,application/xml,text/xml,*/*',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    cookies_content = os.getenv("YOUTUBE_COOKIES")
    cookies_path = None
    opener = urllib.request.build_opener()

    if cookies_content:
        print(f"   🔑 Using YouTube cookies for RSS feed ({len(cookies_content)} chars)")
        try:
            tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
            tmp.write(cookies_content)
            tmp.close()
            cookies_path = tmp.name
            cj = http.cookiejar.MozillaCookieJar(cookies_path)
            cj.load(ignore_discard=True, ignore_expires=True)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        except Exception as ce:
            print(f"⚠️  Cookie load failed: {ce}")
    else:
        print("   No YouTube cookies configured for RSS feed")

    rss_ok = False
    entries = []
    try:
        req = urllib.request.Request(RSS_FEED_URL, headers=headers)
        with opener.open(req, timeout=30) as resp:
            status = resp.getcode()
            xml_content = resp.read()
        print(f"   RSS feed HTTP {status}, {len(xml_content)} bytes")
        root = ET.fromstring(xml_content)
        for entry in root.findall('atom:entry', ns):
            video_id_el = entry.find('yt:videoId', ns)
            if video_id_el is None or not video_id_el.text:
                continue
            video_id = video_id_el.text
            title_el = entry.find('atom:title', ns)
            title = title_el.text if title_el is not None else ''
            link_el = entry.find('atom:link', ns)
            link = link_el.get('href', '') if link_el is not None else f"https://www.youtube.com/watch?v={video_id}"
            published_el = entry.find('atom:published', ns)
            pub_dt = datetime.now(timezone.utc).replace(tzinfo=None)
            if published_el is not None and published_el.text:
                try:
                    pub_dt = datetime.fromisoformat(published_el.text.replace('Z', '+00:00')).replace(tzinfo=None)
                except ValueError:
                    pass
            entries.append(_Entry(f'yt:video:{video_id}', title, link, pub_dt.timetuple()))
        rss_ok = True
        print(f"   ✅ RSS feed returned {len(entries)} entries")
    except Exception as e:
        print(f"⚠️  RSS feed fetch failed: {e} — trying yt-dlp fallback")
    finally:
        if cookies_path:
            try:
                os.unlink(cookies_path)
            except OSError:
                pass

    if not rss_ok or not entries:
        print("   🔄 Switching to yt-dlp for video discovery")
        entries = _get_feed_via_ytdlp()

    return entries


def get_video_transcript(video_url):
    """Get transcript using youtube-transcript-api v1.2+ with proxy support."""
    import tempfile
    import requests as req_lib
    from http.cookiejar import MozillaCookieJar
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.proxies import GenericProxyConfig

    video_id_match = re.search(r'(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})', video_url)
    if not video_id_match:
        print(f"⚠️  Could not extract video ID from {video_url}")
        return None
    video_id = video_id_match.group(1)

    cookies_content = os.getenv("YOUTUBE_COOKIES")
    proxy_url = os.getenv("PROXY_URL")
    tmp_path = None

    # Build session with cookies if available
    session = req_lib.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    })

    if cookies_content:
        print(f"   🔑 Using YouTube cookies ({len(cookies_content)} chars)")
        try:
            tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
            tmp.write(cookies_content)
            tmp.close()
            tmp_path = tmp.name
            cj = MozillaCookieJar(tmp_path)
            cj.load(ignore_discard=True, ignore_expires=True)
            session.cookies = cj  # Direct assignment preserves domain/path metadata
        except Exception as e:
            print(f"⚠️  Cookie load failed: {e}")
    else:
        print("   No YouTube cookies configured")

    # Proxy config bypasses datacenter IP blocks (required on GitHub Actions)
    proxy_config = None
    if proxy_url:
        print(f"   🌐 Using proxy: {proxy_url[:40]}...")
        proxy_config = GenericProxyConfig(http_url=proxy_url, https_url=proxy_url)
    else:
        print("   ⚠️  No PROXY_URL set — GitHub Actions IPs are blocked by YouTube")

    ytt = YouTubeTranscriptApi(
        proxy_config=proxy_config,
        http_client=session,
    )

    try:
        transcript = ytt.fetch(video_id, languages=['en'])
        text = ' '.join(snippet.text for snippet in transcript)
        deduped = re.sub(r'(\b\S+\b)( \1\b)+', r'\1', text)
        print(f"   ✅ Got transcript ({len(deduped)} chars)")
        return deduped[:8000]
    except Exception as e:
        print(f"⚠️  Transcript fetch failed for {video_url}: {type(e).__name__}: {e.__class__.__module__}")
        print("   🔄 Trying yt-dlp for transcript...")
        return _get_transcript_via_ytdlp(video_id, cookies_content, proxy_url)
    finally:
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass


def _get_transcript_via_ytdlp(video_id, cookies_content=None, proxy_url=None):
    """Fallback transcript extraction using yt-dlp auto-generated captions."""
    import subprocess
    import tempfile
    import shutil
    import glob as glob_mod

    out_dir = tempfile.mkdtemp()
    cookies_path = None

    cmd = [
        "yt-dlp",
        "--write-auto-subs", "--sub-lang", "en",
        "--convert-subs", "vtt",
        "--skip-download",
        "--no-warnings", "--quiet",
        "-o", f"{out_dir}/%(id)s",
        f"https://www.youtube.com/watch?v={video_id}",
    ]

    if proxy_url:
        cmd += ["--proxy", proxy_url]

    if cookies_content:
        try:
            tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
            tmp.write(cookies_content)
            tmp.close()
            cookies_path = tmp.name
            cmd += ["--cookies", cookies_path]
        except Exception as e:
            print(f"   ⚠️  yt-dlp cookie setup failed: {e}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        vtt_files = glob_mod.glob(f"{out_dir}/*.vtt")
        if not vtt_files:
            err = result.stderr.strip()[:200] if result.stderr else "(no stderr)"
            print(f"   ⚠️  yt-dlp found no VTT file. stderr: {err}")
            return None

        with open(vtt_files[0]) as f:
            vtt = f.read()

        lines = []
        for line in vtt.split('\n'):
            line = line.strip()
            if not line or line.startswith('WEBVTT') or '-->' in line or line.isdigit():
                continue
            line = re.sub(r'<[^>]+>', '', line)
            if line:
                lines.append(line)

        deduped = []
        prev = None
        for line in lines:
            if line != prev:
                deduped.append(line)
                prev = line

        text = ' '.join(deduped)
        print(f"   ✅ yt-dlp transcript ({len(text)} chars)")
        return text[:8000] if text else None
    except Exception as e:
        print(f"   ⚠️  yt-dlp transcript failed: {e}")
        return None
    finally:
        if cookies_path:
            try:
                os.unlink(cookies_path)
            except OSError:
                pass
        shutil.rmtree(out_dir, ignore_errors=True)


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

        print(f"   📅 {video_id} published {published.strftime('%Y-%m-%d')} — {'already processed' if video_id in processed_videos else 'NEW'}")
        if video_id not in processed_videos:
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
        recipient = os.getenv("EMAIL_RECIPIENT", "eadar7207@gmail.com")

        # Send one email per video
        for video in analyzed_videos:
            subject = f"🎬 {video['title'][:60]}"
            html_content = format_email_html([video])
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

