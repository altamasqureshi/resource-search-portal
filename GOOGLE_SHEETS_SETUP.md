# Google Sheets Migration Setup Guide

## Prerequisites
Your app has been migrated from CSV files to Google Sheets. Follow these steps to complete the setup.

## Step 1: Create Google Sheets

Create three Google Sheets with the following structure:

### 1. Drivers Sheet
- **Columns**: `Model No` | `Driver download Link`
- Copy data from `drivers.csv` to this sheet

### 2. Info Links Sheet
- **Columns**: `Name` | `Link` | `Type`
- Copy data from `info_links.csv` to this sheet

### 3. New Submissions Sheet
- **Columns**: `Timestamp` | `IP Address` | `Name` | `Link` | `Type`
- Copy data from `new_submissions.csv` to this sheet (optional)

## Step 2: Get Google Sheets IDs

For each sheet, copy the ID from the URL:
```
https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit
                                      ^^^^^^^^^^^^^^^^^^^^
```

## Step 3: Create Google Cloud Project & Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"
4. Enable Google Drive API (same process)
5. Create Service Account:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Give it a name (e.g., "printer-driver-app")
   - Click "Create and Continue"
   - Skip optional steps, click "Done"
6. Create Service Account Key:
   - Click on the service account you just created
   - Go to "Keys" tab
   - Click "Add Key" > "Create new key"
   - Choose "JSON" format
   - Download the file and save it as `credentials.json` in your project root

## Step 4: Share Sheets with Service Account

1. Open the downloaded `credentials.json` file
2. Find the `client_email` field (looks like: `your-service@project.iam.gserviceaccount.com`)
3. Share each of your three Google Sheets with this email address:
   - Open each Google Sheet
   - Click "Share" button
   - Paste the service account email
   - Give "Editor" permission
   - Uncheck "Notify people"
   - Click "Share"

## Step 5: Update Configuration

Edit `config.py` and replace the placeholder values:

```python
DRIVERS_SPREADSHEET_ID = 'paste_your_drivers_sheet_id_here'
INFO_LINKS_SPREADSHEET_ID = 'paste_your_info_links_sheet_id_here'
NEW_SUBMISSIONS_SPREADSHEET_ID = 'paste_your_new_submissions_sheet_id_here'

# Update sheet names if different from 'Sheet1'
DRIVERS_SHEET_NAME = 'Sheet1'
INFO_LINKS_SHEET_NAME = 'Sheet1'
NEW_SUBMISSIONS_SHEET_NAME = 'Sheet1'
```

## Step 6: Install Dependencies

Run:
```bash
pip install -r requirements.txt
```

## Step 7: Test the Application

Run your app:
```bash
python app.py
```

The app will now:
- Load data from Google Sheets instead of CSV files
- Automatically reload data at 4 AM daily
- Save new submissions directly to Google Sheets

## Benefits of Google Sheets

✅ Real-time updates - edit sheets and changes reflect in the app
✅ Collaborative editing - multiple people can update data
✅ No need to restart the app when data changes
✅ Automatic backups and version history
✅ Access from anywhere

## Troubleshooting

**Error: "Failed to connect to Google Sheets"**
- Check that `credentials.json` is in the project root
- Verify Google Sheets API and Drive API are enabled
- Ensure service account email has access to all sheets

**Error: "Spreadsheet not found"**
- Double-check the spreadsheet IDs in `config.py`
- Verify the service account has been granted access

**No data loading**
- Check that column names in Google Sheets match exactly:
  - Drivers: `Model No`, `Driver download Link`
  - Info Links: `Name`, `Link`, `Type`
  - New Submissions: `Timestamp`, `IP Address`, `Name`, `Link`, `Type`
