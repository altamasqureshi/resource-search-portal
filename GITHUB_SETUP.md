# GitHub Setup Guide

## Step 1: Install Git

### Download Git for Windows
1. Go to: https://git-scm.com/download/win
2. Download the installer
3. Run the installer with default settings
4. Restart your terminal/command prompt

### Verify Installation
```bash
git --version
```

## Step 2: Configure Git

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use your GitHub email)
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

## Step 3: Create GitHub Account

1. Go to https://github.com
2. Sign up for a free account
3. Verify your email address

## Step 4: Initialize Git Repository (Local)

Open terminal in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files to staging
git add .

# Create first commit
git commit -m "Initial commit: Driver search app with Vercel config"

# Check status
git status
```

## Step 5: Create Repository on GitHub

### Option A: Using GitHub Website
1. Go to https://github.com/new
2. Repository name: `driver-search-app` (or your preferred name)
3. Description: "Flask app for searching printer drivers with Google Sheets integration"
4. Choose: **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option B: Using GitHub CLI (if installed)
```bash
gh repo create driver-search-app --public --source=. --remote=origin
```

## Step 6: Connect Local Repository to GitHub

After creating the repo on GitHub, you'll see commands like these. Run them:

```bash
# Add GitHub as remote origin
git remote add origin https://github.com/YOUR_USERNAME/driver-search-app.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

## Step 7: Verify Upload

1. Go to your GitHub repository URL
2. You should see all your files (except those in .gitignore)
3. Verify that `credentials.json` is NOT visible (it's in .gitignore)

## Step 8: Connect to Vercel

Now that your code is on GitHub:

1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Authorize Vercel to access your GitHub account
4. Select your `driver-search-app` repository
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
6. Add Environment Variables:
   - Click "Environment Variables"
   - Add `SECRET_KEY`: any random string
   - Add `GOOGLE_CREDENTIALS`: paste entire credentials.json content
7. Click "Deploy"

## Step 9: Future Updates

Whenever you make changes:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with a message
git commit -m "Description of what you changed"

# Push to GitHub
git push

# Vercel automatically deploys! 🎉
```

## Common Git Commands

```bash
# Check status
git status

# Add specific file
git add filename.py

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# View remote URL
git remote -v
```

## Troubleshooting

### "git is not recognized"
- Git is not installed or not in PATH
- Restart terminal after installing Git
- Reinstall Git with default settings

### "Permission denied (publickey)"
- Set up SSH keys or use HTTPS URL
- For HTTPS: `git remote set-url origin https://github.com/USERNAME/REPO.git`

### "Failed to push"
- Make sure you committed changes: `git commit -m "message"`
- Pull first if needed: `git pull origin main`
- Check remote URL: `git remote -v`

### "credentials.json appears in GitHub"
- Remove it: `git rm --cached credentials.json`
- Commit: `git commit -m "Remove credentials.json"`
- Push: `git push`
- Verify .gitignore includes `credentials.json`

## Security Checklist

Before pushing to GitHub, verify:

- [ ] `credentials.json` is in .gitignore
- [ ] No API keys or secrets in code
- [ ] `.env` files are in .gitignore (if you use them)
- [ ] Sensitive data is in environment variables, not hardcoded

## Next Steps

After GitHub setup:
1. ✓ Code is on GitHub
2. ✓ Connected to Vercel
3. ✓ Auto-deployment enabled
4. Share your repository URL with collaborators
5. Set up branch protection rules (optional)
6. Enable GitHub Actions for CI/CD (optional)

---

**Your Repository URL will be:**
`https://github.com/YOUR_USERNAME/driver-search-app`

**Your Vercel App URL will be:**
`https://driver-search-app.vercel.app` (or similar)
