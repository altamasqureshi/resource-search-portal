# Vercel Deployment Checklist ✓

## Before You Deploy

- [ ] You have a Vercel account (sign up at https://vercel.com)
- [ ] Node.js is installed (for Vercel CLI)
- [ ] Your `credentials.json` file is ready
- [ ] Your Google Sheets are set up and accessible by the service account

## Deployment Steps

### 1. Install Vercel CLI
```bash
npm install -g vercel
```
- [ ] Vercel CLI installed successfully

### 2. Login to Vercel
```bash
vercel login
```
- [ ] Logged in successfully

### 3. Initial Deployment
```bash
vercel
```
- [ ] Deployment completed
- [ ] Preview URL received and tested

### 4. Set Environment Variables

#### SECRET_KEY
```bash
vercel env add SECRET_KEY
```
Value: Any random string (e.g., `flask-secret-key-xyz123`)
- [ ] SECRET_KEY added

#### GOOGLE_CREDENTIALS
```bash
vercel env add GOOGLE_CREDENTIALS
```
Value: Entire contents of `credentials.json` file
- [ ] GOOGLE_CREDENTIALS added
- [ ] Selected all environments (Production, Preview, Development)

### 5. Production Deployment
```bash
vercel --prod
```
- [ ] Production deployment completed
- [ ] Production URL received

### 6. Testing

Visit your production URL and test:
- [ ] Homepage loads correctly
- [ ] Search functionality works
- [ ] Can submit new items
- [ ] Google Sheets integration works (check your spreadsheet)
- [ ] No errors in Vercel logs (`vercel logs`)

## Post-Deployment

### Optional: Add Custom Domain
1. Go to https://vercel.com/dashboard
2. Select your project
3. Go to Settings → Domains
4. Add your domain
- [ ] Custom domain added (if applicable)

### Monitor Your App
- [ ] Bookmark your Vercel dashboard: https://vercel.com/dashboard
- [ ] Check Analytics tab for usage stats
- [ ] Review logs periodically: `vercel logs`

## Automatic Data Reload

Your app is configured with a Vercel Cron Job that runs daily at 4 AM UTC to reload data from Google Sheets.

To verify:
1. Go to Vercel Dashboard → Your Project → Settings → Cron Jobs
2. You should see: `/api/reload-data` scheduled for `0 4 * * *`

- [ ] Cron job is visible in dashboard

## Troubleshooting

If something goes wrong:

1. **Check logs first:**
   ```bash
   vercel logs
   ```

2. **Verify environment variables:**
   ```bash
   vercel env ls
   ```

3. **Common fixes:**
   - Redeploy: `vercel --prod`
   - Check Google Sheets permissions
   - Verify credentials.json content in environment variable

## Useful Commands Reference

```bash
vercel                    # Deploy to preview
vercel --prod            # Deploy to production
vercel logs              # View logs
vercel env ls            # List environment variables
vercel env add NAME      # Add environment variable
vercel env rm NAME       # Remove environment variable
vercel domains           # Manage domains
vercel --help            # Get help
```

## Success! 🎉

Your Flask app is now live on Vercel!

- Production URL: ___________________________
- Dashboard: https://vercel.com/dashboard
- Deployed on: ___________________________

## Next Steps

1. Share your app URL with users
2. Monitor performance in Vercel dashboard
3. Set up custom domain (optional)
4. Configure alerts for errors (in Vercel settings)
5. Consider upgrading Vercel plan if you need more features

---

Need help? Check:
- QUICK_START_VERCEL.md - Quick deployment guide
- VERCEL_DEPLOYMENT.md - Detailed deployment documentation
- Vercel Docs: https://vercel.com/docs
