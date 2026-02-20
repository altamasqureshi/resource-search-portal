# 🚀 START HERE - Complete Setup Guide

Follow these steps in order to get your app on GitHub and deployed to Vercel.

## ✅ Step 1: Install Git (5 minutes)

1. Download Git: https://git-scm.com/download/win
2. Run installer (use all default settings)
3. Restart your terminal/command prompt
4. Verify: Open terminal and type `git --version`

**If you see a version number, Git is installed! ✓**

## ✅ Step 2: Configure Git (2 minutes)

Open terminal in your project folder and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

## ✅ Step 3: Create GitHub Account (3 minutes)

1. Go to https://github.com
2. Click "Sign up"
3. Follow the registration process
4. Verify your email

## ✅ Step 4: Initialize Git Repository (1 minute)

In your project folder terminal:

```bash
git init
git add .
git commit -m "Initial commit: Driver search app with Vercel config"
```

**Your local repository is ready! ✓**

## ✅ Step 5: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Repository name: `driver-search-app`
3. Description: "Flask app for searching printer drivers"
4. Choose Public or Private
5. **DO NOT check** "Initialize with README" (we already have files)
6. Click "Create repository"

**Keep this page open - you'll need the commands shown!**

## ✅ Step 6: Connect Local to GitHub (1 minute)

GitHub will show you commands like this. Copy and run them:

```bash
git remote add origin https://github.com/YOUR_USERNAME/driver-search-app.git
git branch -M main
git push -u origin main
```

**Replace YOUR_USERNAME with your actual GitHub username!**

After running these, refresh your GitHub repository page. You should see all your files!

## ✅ Step 7: Deploy to Vercel (5 minutes)

### 7a. Create Vercel Account
1. Go to https://vercel.com
2. Click "Sign Up"
3. Choose "Continue with GitHub"
4. Authorize Vercel

### 7b. Import Your Repository
1. Click "Add New..." → "Project"
2. Find your `driver-search-app` repository
3. Click "Import"

### 7c. Configure Project
- Framework Preset: **Other**
- Root Directory: **./  (leave as is)**
- Build Command: **(leave empty)**
- Output Directory: **(leave empty)**

### 7d. Add Environment Variables
Click "Environment Variables" and add:

**Variable 1:**
- Name: `SECRET_KEY`
- Value: `flask-secret-key-xyz123` (or any random string)

**Variable 2:**
- Name: `GOOGLE_CREDENTIALS`
- Value: Open your `credentials.json` file, copy EVERYTHING, paste here

Select "Production, Preview, and Development" for both.

### 7e. Deploy!
Click "Deploy"

Wait 1-2 minutes. Vercel will give you a URL like:
`https://driver-search-app-abc123.vercel.app`

**Visit the URL and test your app! 🎉**

## ✅ Step 8: Test Everything (3 minutes)

Visit your Vercel URL and test:
- [ ] Homepage loads
- [ ] Search works
- [ ] Can submit new items
- [ ] Check your Google Sheet - new submission should appear

## 🎊 You're Done!

Your app is now:
- ✓ Version controlled with Git
- ✓ Backed up on GitHub
- ✓ Live on the internet via Vercel
- ✓ Auto-deploys when you push changes

## 📝 Making Updates (Future)

Whenever you want to update your app:

```bash
# 1. Make your code changes in your editor

# 2. Save and commit
git add .
git commit -m "Describe what you changed"

# 3. Push to GitHub
git push

# 4. Vercel automatically deploys! (30 seconds later)
```

## 📚 Additional Resources

- **Git Commands**: See `GIT_COMMANDS.txt`
- **Detailed GitHub Guide**: See `GITHUB_SETUP.md`
- **Vercel Documentation**: See `VERCEL_DEPLOYMENT.md`
- **Quick Vercel Guide**: See `QUICK_START_VERCEL.md`

## 🆘 Need Help?

### Git not recognized?
- Restart your terminal after installing Git
- Make sure you installed from https://git-scm.com

### Can't push to GitHub?
- Check you used the correct repository URL
- Make sure you're logged into GitHub
- Try: `git remote -v` to see your remote URL

### Vercel deployment failed?
- Check logs in Vercel dashboard
- Verify environment variables are set
- Make sure `GOOGLE_CREDENTIALS` has the complete JSON

### credentials.json visible on GitHub?
```bash
git rm --cached credentials.json
git commit -m "Remove credentials"
git push
```

## 🔗 Your URLs

After setup, bookmark these:

- **GitHub Repo**: https://github.com/YOUR_USERNAME/driver-search-app
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Live App**: (Vercel will provide this)

---

**Estimated Total Time: 20-25 minutes**

Good luck! 🚀
