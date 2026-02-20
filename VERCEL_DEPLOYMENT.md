# Vercel Deployment Guide

## Prerequisites
1. Install Vercel CLI: `npm install -g vercel`
2. Create a Vercel account at https://vercel.com

## Deployment Steps

### 1. Login to Vercel
```bash
vercel login
```

### 2. Deploy to Vercel
```bash
vercel
```
Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N**
- Project name? (press Enter for default or type a name)
- In which directory is your code located? **.**
- Want to override settings? **N**

### 3. Set Environment Variables
After deployment, you need to add your Google Sheets credentials:

#### Option A: Using Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Select your project
3. Go to Settings → Environment Variables
4. Add these variables:
   - `SECRET_KEY`: A random secret key for Flask sessions
   - `GOOGLE_CREDENTIALS`: Paste the entire contents of your `credentials.json` file

#### Option B: Using Vercel CLI
```bash
vercel env add SECRET_KEY
vercel env add GOOGLE_CREDENTIALS
```

### 4. Update config.py for Vercel
You'll need to modify `config.py` to read credentials from environment variable:

```python
import os
import json

# For Vercel deployment, credentials come from environment variable
if os.environ.get('GOOGLE_CREDENTIALS'):
    CREDENTIALS_FILE = None
    CREDENTIALS_JSON = json.loads(os.environ.get('GOOGLE_CREDENTIALS'))
else:
    CREDENTIALS_FILE = 'credentials.json'
    CREDENTIALS_JSON = None
```

### 5. Update sheets_helper.py
Modify the initialization to handle environment credentials.

### 6. Redeploy
```bash
vercel --prod
```

## Important Notes

### Background Scheduler Limitation
Vercel uses serverless functions, which don't support background schedulers. To reload data periodically:

**Option 1: Vercel Cron Jobs**
Create `vercel.json` with cron configuration:
```json
{
  "crons": [{
    "path": "/api/reload",
    "schedule": "0 4 * * *"
  }]
}
```

**Option 2: External Service**
Use GitHub Actions, AWS Lambda, or other services to trigger data reload via API endpoint.

**Option 3: Reload on Each Request**
Add caching with TTL to reload data after a certain time period.

### Static Files
Ensure your `templates/` folder is included in the deployment.

### Logs
Vercel has its own logging system. View logs at:
- Dashboard: https://vercel.com/dashboard → Your Project → Logs
- CLI: `vercel logs`

## Testing
After deployment, Vercel will provide a URL like:
`https://your-project-name.vercel.app`

Test your application at this URL.

## Custom Domain (Optional)
1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

## Troubleshooting

### Issue: Module not found
- Ensure all dependencies are in `requirements.txt`
- Redeploy: `vercel --prod`

### Issue: Google Sheets authentication fails
- Verify `GOOGLE_CREDENTIALS` environment variable is set correctly
- Check that the service account has access to your sheets

### Issue: 500 Internal Server Error
- Check logs: `vercel logs`
- Verify all environment variables are set

## Useful Commands
- `vercel`: Deploy to preview
- `vercel --prod`: Deploy to production
- `vercel logs`: View logs
- `vercel env ls`: List environment variables
- `vercel domains`: Manage domains
