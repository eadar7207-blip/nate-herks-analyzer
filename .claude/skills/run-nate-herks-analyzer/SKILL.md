---
name: run-nate-herks-analyzer
description: Monitor Nate Herks videos, analyze with AI, and get daily email summaries
---

# Nate Herks Video Analyzer

Automatically analyze new Nate Herks YouTube videos and receive detailed daily email summaries highlighting key points and AI real estate insights.

## Setup Status

Your analyzer is configured to run automatically every day at 8:00 AM UTC via GitHub Actions.

**GitHub Repo:** https://github.com/eadar7207-blip/nate-herks-analyzer

## What It Does

- ✅ Monitors Nate Herks' YouTube channel daily
- 📹 Downloads transcripts from new videos  
- 🧠 Uses Claude AI to analyze content
- 📊 Highlights breakthroughs relevant to AI real estate
- 📧 Sends detailed HTML email summaries
- 🤖 Runs completely automated

## Configuration

All 4 secrets are already set up:
- ✅ ANTHROPIC_API_KEY
- ✅ EMAIL_SENDER
- ✅ EMAIL_PASSWORD
- ✅ EMAIL_RECIPIENT

## Manual Trigger

To run the analyzer manually right now:

```bash
curl -X POST https://api.github.com/repos/eadar7207-blip/nate-herks-analyzer/actions/workflows/analyze.yml/dispatches \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"ref":"main"}'
```

Replace `YOUR_GITHUB_TOKEN` with a personal access token from https://github.com/settings/tokens

Or simply go to: **https://github.com/eadar7207-blip/nate-herks-analyzer/actions**
- Click "Daily Nate Herks Analysis"
- Click "Run workflow"

## Check Recent Analyses

View all automated runs here:
**https://github.com/eadar7207-blip/nate-herks-analyzer/actions**

Each run shows:
- Video analyzed
- Analysis results
- Email status

## Change Schedule

To change the daily run time, edit `.github/workflows/analyze.yml`:

```yaml
- cron: '0 8 * * *'  # Change 8 to your preferred hour (0-23)
```

Current schedule: **8:00 AM UTC daily**

## Local Testing

To test locally:

```bash
cd ~/nate-herks-analyzer
export ANTHROPIC_API_KEY="your-key-here"
export EMAIL_SENDER="your.email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export EMAIL_RECIPIENT="your.email@gmail.com"
python analyzer.py
```

## Files

- `analyzer.py` — Main analysis script
- `requirements.txt` — Python dependencies
- `.github/workflows/analyze.yml` — GitHub Actions schedule
- `README.md` — Full documentation
- `SETUP_CHECKLIST.md` — Setup guide

## Logs

Check the GitHub Actions logs for:
- Video detection results
- Analysis details
- Email sending status
- Error messages

## Next Steps

1. **Wait for tomorrow** - First automated run is tomorrow at 8 AM UTC
2. **Check your email** - You'll receive the analysis summary
3. **Adjust as needed** - Modify the schedule, analysis prompt, or email format

Your analyzer is now **active and automated**! 🚀
