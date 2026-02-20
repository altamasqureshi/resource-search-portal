import gspread
from google.oauth2.service_account import Credentials
from logger import setup_logging
import os
import json

logger = setup_logging()

class GoogleSheetsHelper:
    def __init__(self, credentials_file='credentials.json', credentials_json=None):
        """
        Initialize Google Sheets connection
        credentials_file: Path to your service account JSON file (for local)
        credentials_json: Dictionary with credentials (for Vercel environment)
        """
        self.credentials_file = credentials_file
        self.credentials_json = credentials_json
        self.client = None
        self._connect()
    
    def _connect(self):
        """Establish connection to Google Sheets"""
        try:
            scopes = [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
            
            # Check if credentials are provided as JSON (Vercel environment)
            if self.credentials_json:
                creds = Credentials.from_service_account_info(self.credentials_json, scopes=scopes)
                logger.info("Using credentials from environment variable")
            # Check if GOOGLE_CREDENTIALS environment variable exists
            elif os.environ.get('GOOGLE_CREDENTIALS'):
                creds_dict = json.loads(os.environ.get('GOOGLE_CREDENTIALS'))
                creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
                logger.info("Using credentials from GOOGLE_CREDENTIALS environment variable")
            # Fall back to credentials file
            else:
                creds = Credentials.from_service_account_file(self.credentials_file, scopes=scopes)
                logger.info("Using credentials from file")
            
            self.client = gspread.authorize(creds)
            logger.info("Successfully connected to Google Sheets")
        except Exception as e:
            logger.error(f"Failed to connect to Google Sheets: {e}")
            raise
    
    def read_sheet(self, spreadsheet_id, sheet_name):
        """
        Read data from a Google Sheet
        Returns list of dictionaries with headers as keys
        """
        try:
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            worksheet = spreadsheet.worksheet(sheet_name)
            data = worksheet.get_all_records()
            logger.info(f"Successfully read {len(data)} rows from {sheet_name}")
            return data
        except Exception as e:
            logger.error(f"Error reading sheet {sheet_name}: {e}")
            return []
    
    def append_row(self, spreadsheet_id, sheet_name, row_data):
        """
        Append a row to a Google Sheet
        row_data: List of values to append
        """
        try:
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            worksheet = spreadsheet.worksheet(sheet_name)
            worksheet.append_row(row_data)
            logger.info(f"Successfully appended row to {sheet_name}")
            return True
        except Exception as e:
            logger.error(f"Error appending row to {sheet_name}: {e}")
            return False
