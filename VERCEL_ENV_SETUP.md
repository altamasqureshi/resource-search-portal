# Vercel Environment Variable Setup

## Critical: Set Up Google Credentials

Your app is crashing because Vercel needs the Google Sheets credentials as an environment variable.

### Steps:

1. **Get your credentials JSON content:**
   - Open `credentials.json` in your local project
   - Copy the ENTIRE content (it should look like a JSON object with `type`, `project_id`, `private_key`, etc.)

2. **Add to Vercel:**
   - Go to your Vercel project dashboard
   - Click on **Settings** tab
   - Click on **Environment Variables** in the left sidebar
   - Add a new variable:
     - **Name:** `GOOGLE_CREDENTIALS_JSON`
     - **Value:** Paste the entire JSON content from credentials.json
     - **Environment:** Select all (Production, Preview, Development)
   - Click **Save**

3. **Add SECRET_KEY (optional but recommended):**
   - Add another environment variable:
     - **Name:** `SECRET_KEY`
     - **Value:** Generate a random string (e.g., use a password generator)
     - **Environment:** Select all
   - Click **Save**

4. **Redeploy:**
   - After saving environment variables, Vercel will automatically redeploy
   - Or manually trigger a redeploy from the Deployments tab

### Verify Setup:

Once deployed, check the Function Logs in Vercel dashboard to see if the app initializes successfully. You should see:
- "Google Sheets helper initialized with environment credentials"
- "Data reloaded: X drivers, Y info links"

### Troubleshooting:

If still getting errors:
- Check Function Logs in Vercel dashboard for specific error messages
- Verify the JSON is valid (no extra quotes or formatting issues)
- Make sure all environment variables are set for Production environment
