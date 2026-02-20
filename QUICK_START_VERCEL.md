# Quick Start: Deploy to Vercel in 5 Minutes

## Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

## Step 2: Login to Vercel
```bash
vercel login
```
This will open your browser to authenticate.

## Step 3: Deploy
```bash
vercel
```
Answer the prompts:
- **Set up and deploy?** → Y
- **Which scope?** → Select your account
- **Link to existing project?** → N
- **Project name?** → Press Enter or type a name
- **In which directory is your code located?** → . (just press Enter)
- **Want to override settings?** → N

Vercel will give you a preview URL like: `https://your-project-abc123.vercel.app`

## Step 4: Add Google Sheets Credentials

### Get your credentials ready:
1. Open `credentials.json` in a text editor
2. Copy the ENTIRE content (it's a JSON object)

### Add to Vercel:
```bash
vercel env add GOOGLE_CREDENTIALS
```
- **What's the value?** → Paste the entire credentials.json content
- **Add to which environment?** → Select all (Production, Preview, Development)

### Add Secret Key:
```bash
vercel env add SECRET_KEY
```
- **What's the value?** → Type any random string (e.g., `my-super-secret-key-12345`)
- **Add to which environment?** → Select all

## Step 5: Deploy to Production
```bash
vercel --prod
```

Your app is now live! Vercel will show you the production URL.

## Step 6: Test Your App
Visit the URL provided by Vercel and test:
- Search functionality
- Submit new items
- Check if Google Sheets integration works

## Troubleshooting

### If you get errors:
1. Check logs:
   ```bash
   vercel logs
   ```

2. Verify environment variables:
   ```bash
   vercel env ls
   ```

3. Make sure your Google Sheets service account has access to the spreadsheet

### Common Issues:

**"Module not found"**
- All dependencies are in requirements.txt, so this shouldn't happen
- Try redeploying: `vercel --prod`

**"Google Sheets authentication failed"**
- Verify GOOGLE_CREDENTIALS is set correctly
- Make sure you pasted the ENTIRE credentials.json content
- Check that the service account email has Editor access to your Google Sheet

**"500 Internal Server Error"**
- Check logs: `vercel logs`
- Verify all environment variables are set

## Managing Your Deployment

### View in Dashboard:
Visit https://vercel.com/dashboard to:
- See deployment status
- View logs
- Manage environment variables
- Add custom domains
- Monitor performance

### Update Your App:
Just run `vercel --prod` again after making changes.

### Roll Back:
In the Vercel dashboard, you can instantly roll back to any previous deployment.

## Next Steps

1. **Add Custom Domain** (optional):
   - Go to Project Settings → Domains
   - Add your domain and follow DNS instructions

2. **Set Up Cron Job** for data reload:
   - See VERCEL_DEPLOYMENT.md for details

3. **Monitor Performance**:
   - Check the Analytics tab in Vercel dashboard

That's it! Your Flask app is now running on Vercel. 🎉
