# 🚀 Setup Checklist

Complete these steps to get your automated Nate Herks analyzer running.

## Step 1: Create GitHub Repository
- [ ] Go to [github.com/new](https://github.com/new)
- [ ] Repository name: `nate-herks-analyzer`
- [ ] Description: "Automated Nate Herks video analysis with AI insights"
- [ ] Make it **Public** (so GitHub Actions can run)
- [ ] Click "Create repository"

## Step 2: Get API Keys
- [ ] **Anthropic API Key**
  - [ ] Go to https://console.anthropic.com
  - [ ] Sign in / Create account
  - [ ] Click "API Keys" (left sidebar)
  - [ ] Click "Create Key"
  - [ ] Copy the key (save it somewhere temporarily)
  
- [ ] **Gmail App Password**
  - [ ] Go to https://myaccount.google.com/security
  - [ ] Enable "2-Step Verification" (if not already enabled)
  - [ ] Go to https://myaccount.google.com/apppasswords
  - [ ] Select "Mail" and "Windows Computer"
  - [ ] Generate & copy the 16-character password

## Step 3: Push Code to GitHub
```bash
cd ~/nate-herks-analyzer
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nate-herks-analyzer.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username.

## Step 4: Add GitHub Secrets
In your GitHub repository:

1. Click **Settings** (top navigation)
2. Click **Secrets and variables** → **Actions** (left sidebar)
3. Click **"New repository secret"** and add these 4 secrets:

### Secret 1: ANTHROPIC_API_KEY
- Name: `ANTHROPIC_API_KEY`
- Value: Paste your Anthropic API key
- [ ] Added

### Secret 2: EMAIL_SENDER
- Name: `EMAIL_SENDER`
- Value: Your Gmail address (e.g., `yourname@gmail.com`)
- [ ] Added

### Secret 3: EMAIL_PASSWORD
- Name: `EMAIL_PASSWORD`
- Value: The 16-character Gmail app password
- [ ] Added

### Secret 4: EMAIL_RECIPIENT
- Name: `EMAIL_RECIPIENT`
- Value: Where to send emails (can be same as EMAIL_SENDER)
- [ ] Added

## Step 5: Enable GitHub Actions
- [ ] Go to **Actions** tab in your repository
- [ ] Click "I understand my workflows, go ahead and enable them"
- [ ] You should see "Daily Nate Herks Analysis" listed

## Step 6: Test It!
- [ ] Go to **Actions** tab
- [ ] Click **"Daily Nate Herks Analysis"**
- [ ] Click **"Run workflow"** button
- [ ] Watch it run (takes 2-5 minutes)
- [ ] Check your email for the analysis!

## Step 7: Automate
Once the test run succeeds, it will automatically run daily at **8:00 AM UTC**.

To change the time, edit `.github/workflows/analyze.yml` and change:
```yaml
- cron: '0 8 * * *'  # Change first number (hour)
```

---

## ✅ All Done!

Your Nate Herks analyzer is now:
- ✅ Monitoring his YouTube channel daily
- ✅ Extracting key insights
- ✅ Emailing you detailed AI real estate analysis
- ✅ Fully automated

Check your email every morning for fresh insights! 📧

---

## 🆘 Something Not Working?

1. Check **Actions** tab → click the failed workflow → read error logs
2. Verify all 4 secrets are correctly set in **Settings** → **Secrets**
3. Try manually running the workflow again
4. See README.md Troubleshooting section

Good luck! 🚀
