# Nate Herks Video Analyzer 🎬

Automatically analyze new Nate Herks YouTube videos and get **detailed daily email summaries** highlighting key points and AI real estate insights.

## What It Does

- ✅ Monitors Nate Herks' YouTube channel **daily**
- 📹 Automatically downloads transcripts from new videos
- 🧠 Uses Claude AI to analyze content and extract insights
- 📊 Highlights breakthroughs relevant to **AI real estate consulting**
- 📧 Sends a **detailed HTML email** each morning with analysis
- 🤖 Runs completely automated via GitHub Actions

## How It Works

```
YouTube Feed → Download Transcript → Claude Analysis → Email Report
     (Daily)        (yt-dlp)         (Claude API)   (Gmail SMTP)
```

## Setup Instructions

### 1. Create GitHub Repository

First, you need to push this project to GitHub:

```bash
cd nate-herks-analyzer
git init
git add .
git commit -m "Initial commit: Nate Herks analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nate-herks-analyzer.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 2. Get Required API Keys & Credentials

#### **Anthropic API Key** (for Claude)
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign in or create account
3. Go to "API Keys" → Generate new API key
4. Copy the key (starts with `sk-ant-...`)

#### **Gmail App Password** (for sending emails)
1. Enable 2-Step Verification on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Select "Mail" and "Windows Computer"
4. Generate app password
5. Copy the 16-character password

### 3. Configure GitHub Secrets

In your GitHub repository:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add these 4 secrets:

| Secret Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from step 2 |
| `EMAIL_SENDER` | Your Gmail address (e.g., your.email@gmail.com) |
| `EMAIL_PASSWORD` | The 16-character Gmail app password from step 2 |
| `EMAIL_RECIPIENT` | Where to send emails (can be same as EMAIL_SENDER or different) |

**Each secret:**
- Click "New repository secret"
- Name: `ANTHROPIC_API_KEY` (or other name from table)
- Value: paste the actual key/password
- Click "Add secret"

### 4. Enable GitHub Actions

1. Go to your repository
2. Click **Actions** tab
3. Click **"I understand my workflows, go ahead and enable them"** (if prompted)
4. The workflow will appear as "Daily Nate Herks Analysis"

### 5. Test It

#### Option A: Manual Run
1. Go to **Actions** tab
2. Click **"Daily Nate Herks Analysis"**
3. Click **"Run workflow"** → **"Run workflow"**
4. Wait 2-5 minutes and check your email

#### Option B: Wait for Schedule
By default, the analyzer runs at **8:00 AM UTC daily**.

To change the time, edit `.github/workflows/analyze.yml`:
```yaml
- cron: '0 8 * * *'  # Change 8 to your preferred hour (0-23)
```

## What You'll Receive

An email like this:

```
Subject: 🎬 Nate Herks Daily Analysis - 1 Video(s)

📹 Video Title
Published: May 31 at 2:30 PM

Key Points Summary
- Point 1
- Point 2
- Point 3

AI Real Estate Breakthrough
How this applies to your AI real estate consultant business...

Actionable Insights
- Implementation idea 1
- Implementation idea 2

Quote or Highlight
"Most impactful quote from the video"
```

## Troubleshooting

### "No emails received"

Check the **Actions** tab in GitHub:
1. Click the failed workflow run
2. Click "analyze" job
3. Look for error messages in the logs

Common issues:
- **Wrong Gmail app password:** Generate new one and update secret
- **2-Step Verification not enabled:** Enable it in Google Account
- **Email recipient typo:** Double-check EMAIL_RECIPIENT secret
- **ANTHROPIC_API_KEY invalid:** Re-generate from console.anthropic.com

### "API request failed"

- Check ANTHROPIC_API_KEY is valid
- Verify you have API credits (check console.anthropic.com)
- Try manual workflow run to see detailed error

### "No new videos analyzed"

- Check if Nate Herks posted in the last 24 hours
- The script only processes videos from the past day
- Try running manually to test

## Manual Running (Local)

To test locally before deployment:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (macOS/Linux)
export ANTHROPIC_API_KEY="sk-ant-..."
export EMAIL_SENDER="your.email@gmail.com"
export EMAIL_PASSWORD="16-character-app-password"
export EMAIL_RECIPIENT="your.email@gmail.com"

# Run
python analyzer.py
```

## File Structure

```
nate-herks-analyzer/
├── .github/workflows/
│   └── analyze.yml           # GitHub Actions schedule & config
├── analyzer.py               # Main analysis script
├── requirements.txt          # Python dependencies
├── .processed_videos.json    # Cache of analyzed videos (auto-generated)
└── README.md                # This file
```

## How the Analysis Works

1. **Fetch Videos:** Checks YouTube RSS feed for Nate Herks' latest videos
2. **Get Transcript:** Downloads auto-generated captions/transcript
3. **AI Analysis:** Sends transcript to Claude API with prompt asking for:
   - Key points summary
   - AI real estate breakthroughs
   - Actionable insights for your business
4. **Format Email:** Creates beautiful HTML email with analysis
5. **Send:** Emails via Gmail SMTP

## Customization

### Change analysis frequency
Edit `.github/workflows/analyze.yml` cron expression:
- `0 8 * * *` = 8 AM UTC daily
- `0 9 * * 1-5` = 9 AM UTC weekdays only
- `0 */12 * * *` = Every 12 hours

### Adjust analysis depth
Edit the prompt in `analyzer.py` function `analyze_video_with_claude()` to ask for different insights.

### Add more metrics
Modify `format_email_html()` to change email layout/styling.

## API Costs

- **Anthropic API:** ~$0.01-0.05 per video (Claude Opus 4)
- **YouTube/GitHub:** Free
- **Gmail:** Free

Total: ~$0.30-1.50 per month for daily analysis

## Support

If you encounter issues:

1. Check GitHub Actions logs: **Repository** → **Actions** → click failed run
2. Verify all secrets are set correctly
3. Test locally with `python analyzer.py` + environment variables
4. Check that Gmail 2-Step Verification is enabled

## License

This project is for personal use. Feel free to modify and extend as needed.

---

**Happy analyzing! 🚀**

Your AI real estate insights are now automated.
