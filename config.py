# Google Sheets Configuration
# Single spreadsheet with multiple tabs/subsheets

# Main spreadsheet ID (from the URL of your Google Sheet)
SPREADSHEET_ID = '1ohtTDY4NXfPM_9g2jJKN1cRYaK591HYFc5mSeitQh0w'

# For backward compatibility (all point to same spreadsheet)
DRIVERS_SPREADSHEET_ID = SPREADSHEET_ID
INFO_LINKS_SPREADSHEET_ID = SPREADSHEET_ID
NEW_SUBMISSIONS_SPREADSHEET_ID = SPREADSHEET_ID

# Sheet names (tab names at the bottom of your spreadsheet)
DRIVERS_SHEET_NAME = 'drivers'
INFO_LINKS_SHEET_NAME = 'info_links'
NEW_SUBMISSIONS_SHEET_NAME = 'new_submissions'

# Service account credentials file
import os
CREDENTIALS_FILE = 'credentials.json'

# For Vercel deployment, use environment variable
GOOGLE_CREDENTIALS_JSON = os.environ.get('GOOGLE_CREDENTIALS_JSON')
