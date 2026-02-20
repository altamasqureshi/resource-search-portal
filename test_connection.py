"""
Test script to verify Google Sheets connection
"""
from sheets_helper import GoogleSheetsHelper
import config

print("=" * 60)
print("Testing Google Sheets Connection")
print("=" * 60)

# Test 1: Check if credentials file exists
print("\n1. Checking credentials file...")
try:
    with open(config.CREDENTIALS_FILE, 'r') as f:
        print("   ✓ credentials.json found")
except FileNotFoundError:
    print("   ✗ credentials.json NOT FOUND!")
    print("   Please make sure credentials.json is in the project folder")
    exit(1)

# Test 2: Initialize Google Sheets connection
print("\n2. Connecting to Google Sheets...")
try:
    sheets = GoogleSheetsHelper(config.CREDENTIALS_FILE)
    print("   ✓ Successfully connected to Google Sheets")
except Exception as e:
    print(f"   ✗ Connection failed: {e}")
    exit(1)

# Test 3: Read drivers sheet
print("\n3. Reading 'drivers' sheet...")
try:
    drivers = sheets.read_sheet(config.DRIVERS_SPREADSHEET_ID, config.DRIVERS_SHEET_NAME)
    print(f"   ✓ Successfully read {len(drivers)} rows from drivers sheet")
    if len(drivers) > 0:
        print(f"   First entry: {drivers[0].get('Model No', 'N/A')}")
except Exception as e:
    print(f"   ✗ Failed to read drivers sheet: {e}")

# Test 4: Read info_links sheet
print("\n4. Reading 'info_links' sheet...")
try:
    info_links = sheets.read_sheet(config.INFO_LINKS_SPREADSHEET_ID, config.INFO_LINKS_SHEET_NAME)
    print(f"   ✓ Successfully read {len(info_links)} rows from info_links sheet")
    if len(info_links) > 0:
        print(f"   First entry: {info_links[0].get('Name', 'N/A')}")
except Exception as e:
    print(f"   ✗ Failed to read info_links sheet: {e}")

# Test 5: Read new_submissions sheet
print("\n5. Reading 'new_submissions' sheet...")
try:
    submissions = sheets.read_sheet(config.NEW_SUBMISSIONS_SPREADSHEET_ID, config.NEW_SUBMISSIONS_SHEET_NAME)
    print(f"   ✓ Successfully read {len(submissions)} rows from new_submissions sheet")
except Exception as e:
    print(f"   ✗ Failed to read new_submissions sheet: {e}")

print("\n" + "=" * 60)
print("Connection test completed!")
print("=" * 60)
print("\nIf all tests passed, you can now run: python app.py")
