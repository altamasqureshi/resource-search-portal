from flask import Flask, render_template, request, redirect, url_for, flash
from fuzzywuzzy import fuzz
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import os

from logger import setup_logging
from sheets_helper import GoogleSheetsHelper
import config

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_super_secret_key')

logger = setup_logging()

all_drivers = []
all_info_links = []
sheets_helper = None

def initialize_sheets():
    """Initialize Google Sheets connection"""
    global sheets_helper
    try:
        sheets_helper = GoogleSheetsHelper(config.CREDENTIALS_FILE)
        logger.info("Google Sheets helper initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Google Sheets: {e}")
        sheets_helper = None

def reload_data():
    """Reload data from Google Sheets"""
    global all_drivers, all_info_links
    
    if sheets_helper is None:
        logger.error("Google Sheets helper not initialized")
        return
    
    all_drivers = []
    all_info_links = []
    
    try:
        # Load drivers from Google Sheets
        drivers_data = sheets_helper.read_sheet(
            config.DRIVERS_SPREADSHEET_ID, 
            config.DRIVERS_SHEET_NAME
        )
        for row in drivers_data:
            all_drivers.append({
                'name': row.get('Model No', ''),
                'link': row.get('Driver download Link', ''),
                'type': 'Printer Driver'
            })
        
        # Load info links from Google Sheets
        info_data = sheets_helper.read_sheet(
            config.INFO_LINKS_SPREADSHEET_ID,
            config.INFO_LINKS_SHEET_NAME
        )
        for row in info_data:
            all_info_links.append({
                'name': row.get('Name', ''),
                'link': row.get('Link', ''),
                'type': row.get('Type', '')
            })
        
        logger.info(f"Google Sheets data reloaded: {len(all_drivers)} drivers, {len(all_info_links)} info links")
    except Exception as e:
        logger.error(f"Error reloading data from Google Sheets: {e}")

def load_data():
    """Initial data load"""
    reload_data()

# Initialize Google Sheets and load data
initialize_sheets()
load_data()

# Setup scheduler (disabled for Vercel serverless environment)
# Note: Background schedulers don't work in serverless environments
# Consider using Vercel Cron Jobs or external services like GitHub Actions
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=reload_data, trigger='cron', hour=4)
# scheduler.start()

def search_items(query):
    results = []
    # Search in all_drivers (in-memory)
    for item in all_drivers:
        item_name = item['name']
        if max(fuzz.token_set_ratio(query.lower(), item_name.lower()), fuzz.partial_ratio(query.lower(), item_name.lower())) >= 70:
            results.append(item)

    # Search in all_info_links (in-memory)
    for item in all_info_links:
        item_name = item['name']
        if max(fuzz.token_set_ratio(query.lower(), item_name.lower()), fuzz.partial_ratio(query.lower(), item_name.lower())) >= 70:
            results.append(item)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        logger.info(f"Search query: {query} from IP: {request.remote_addr}")
        results = search_items(query)
    return render_template('index.html', results=results)

@app.route('/submit', methods=['POST'])
def submit():
    item_name = request.form['item_name']
    item_link = request.form['item_link']
    item_type = request.form['item_type']
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    logger.info(f"New submission: {item_name}, {item_link}, {item_type} from IP: {ip_address}")

    try:
        if sheets_helper:
            success = sheets_helper.append_row(
                config.NEW_SUBMISSIONS_SPREADSHEET_ID,
                config.NEW_SUBMISSIONS_SHEET_NAME,
                [timestamp, ip_address, item_name, item_link, item_type]
            )
            if success:
                flash('Your submission has been received and is pending review.', 'success')
            else:
                flash('Error submitting your request. Please try again.', 'error')
        else:
            flash('Google Sheets connection not available.', 'error')
    except Exception as e:
        logger.error(f"Error adding item: {e}")
        flash(f'Error adding item: {e}', 'error')

    return redirect(url_for('index'))

@app.route('/api/reload-data', methods=['GET', 'POST'])
def api_reload_data():
    """API endpoint for Vercel Cron Jobs to reload data"""
    try:
        reload_data()
        logger.info("Data reloaded via API endpoint")
        return {'status': 'success', 'message': 'Data reloaded successfully'}, 200
    except Exception as e:
        logger.error(f"Error reloading data via API: {e}")
        return {'status': 'error', 'message': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')