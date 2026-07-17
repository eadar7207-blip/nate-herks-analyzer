#!/usr/bin/env python3
"""
Send latest_analysis.md as a formatted HTML email.
Used when the main analyzer has pre-written analysis but no SMTP access locally.
Reads EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT from environment.
"""

import os
import re
import smtplib
from datetime import datetime
from html import escape
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


def md_to_html(md: str) -> str:
    """Convert the analyzer's markdown format to HTML sections."""
    html_parts = []
    in_list = False
    in_video_block = False

    for line in md.split('\n'):
        s = line.rstrip()

        # H1 date headings become section dividers
        if s.startswith('# Nate Herk Analysis'):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            if in_video_block:
                html_parts.append('</div>')
                in_video_block = False
            date = s.replace('# Nate Herk Analysis —', '').strip()
            html_parts.append(f'<div class="date-divider">{escape(date)}</div>')
            continue

        # H2 video titles
        if s.startswith('## '):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            if in_video_block:
                html_parts.append('</div>')
            in_video_block = True
            # Extract link markdown [title](url)
            m = re.match(r'## \[(.+?)\]\((.+?)\)', s)
            if m:
                title, url = m.group(1), m.group(2)
                html_parts.append(
                    f'<div class="video"><h2><a href="{escape(url)}" target="_blank">{escape(title)}</a></h2>'
                )
            else:
                html_parts.append(f'<div class="video"><h2>{escape(s[3:])}</h2>')
            continue

        # Italic date line *...*
        if s.startswith('*') and s.endswith('*') and len(s) > 2:
            html_parts.append(f'<p class="pub-date">{escape(s[1:-1])}</p>')
            continue

        # HR divider
        if s == '---':
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            continue

        # All-caps section headings (WHAT IT'S ABOUT, THE KEY POINTS, etc.)
        if s and s == s.upper() and re.match(r'^[A-Z\s\'\-]+$', s) and len(s) > 3:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(
                f'<h3>{escape(s)}</h3>'
            )
            continue

        # Bullet points
        if s.startswith('- ') or s.startswith('• '):
            if not in_list:
                html_parts.append('<ul>')
                in_list = True
            content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(s[2:]))
            html_parts.append(f'<li>{content}</li>')
            continue

        # Empty line
        if not s:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            continue

        # Normal paragraph
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(s))
        html_parts.append(f'<p>{content}</p>')

    if in_list:
        html_parts.append('</ul>')
    if in_video_block:
        html_parts.append('</div>')

    return '\n'.join(html_parts)


def build_email_html(analysis_md: str, date_str: str) -> str:
    body = md_to_html(analysis_md)
    return f"""<html>
<head>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
         line-height: 1.6; color: #333; margin: 0; padding: 0; }}
  .container {{ max-width: 620px; margin: 0 auto; padding: 20px; }}
  .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
             color: white; padding: 24px; border-radius: 8px; margin-bottom: 28px; }}
  .header h1 {{ margin: 0 0 4px 0; font-size: 24px; }}
  .header p {{ margin: 0; opacity: 0.9; font-size: 14px; }}
  .date-divider {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em;
                   color: #999; margin: 32px 0 12px 0; border-top: 1px solid #eee;
                   padding-top: 12px; }}
  .video {{ border-left: 4px solid #667eea; padding-left: 20px; margin-bottom: 40px; }}
  .video h2 {{ margin-top: 0; color: #667eea; font-size: 17px; }}
  .video a {{ color: #667eea; text-decoration: none; }}
  .video a:hover {{ text-decoration: underline; }}
  .pub-date {{ font-size: 12px; color: #999; margin-top: -8px; margin-bottom: 12px; }}
  h3 {{ color: #444; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em;
        margin: 18px 0 6px 0; }}
  p {{ margin: 6px 0; font-size: 14px; }}
  ul {{ margin: 6px 0; padding-left: 20px; }}
  li {{ margin: 5px 0; font-size: 14px; }}
  .footer {{ margin-top: 40px; padding-top: 16px; border-top: 1px solid #ddd;
             font-size: 11px; color: #aaa; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>🎬 Nate Herk Daily Analysis</h1>
    <p>{escape(date_str)}</p>
  </div>
  {body}
  <div class="footer">
    <p>Automatically generated by your Nate Herks Video Analyzer · Powered by Claude AI</p>
  </div>
</div>
</body>
</html>"""


def send_email(recipient: str, subject: str, html_content: str) -> bool:
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("⚠️  EMAIL_SENDER or EMAIL_PASSWORD not set — cannot send email")
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


def main():
    import sys
    analysis_path = Path(__file__).parent / "latest_analysis.md"
    if not analysis_path.exists():
        print("❌ latest_analysis.md not found")
        sys.exit(1)

    analysis_md = analysis_path.read_text(encoding="utf-8")
    if not analysis_md.strip():
        print("⚠️  latest_analysis.md is empty — nothing to send")
        sys.exit(1)

    date_str = datetime.now().strftime("%B %d, %Y")
    recipient = os.getenv("EMAIL_RECIPIENT", "eadar7207@gmail.com")
    subject = f"🎬 Nate Herk Analysis — {date_str}"
    html_content = build_email_html(analysis_md, date_str)

    print(f"📧 Sending analysis email to {recipient}…")
    if not send_email(recipient, subject, html_content):
        sys.exit(1)


if __name__ == "__main__":
    main()
