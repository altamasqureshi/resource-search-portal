import csv
from flask import Flask, render_template, request, redirect, url_for, flash
from fuzzywuzzy import fuzz
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler # New import

from logger import setup_logging

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' # Replace with a strong, random key in production

logger = setup_logging()

all_drivers = []
all_info_links = []

def reload_data(): # New function for scheduled reload
    global all_drivers, all_info_links
    all_drivers = []
    all_info_links = []
    with open('drivers.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            all_drivers.append({'name': row[0], 'link': row[1], 'type': 'Printer Driver'})

    with open('info_links.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            all_info_links.append({'name': row[0], 'link': row[1], 'type': row[2]})
    logger.info("CSV data reloaded successfully.")

def load_data(): # Modified to call reload_data
    reload_data()

load_data() # Initial load

# Setup scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=reload_data, trigger='cron', hour=4) # Schedule for 4 AM daily
scheduler.start()

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
        with open('new_submissions.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, ip_address, item_name, item_link, item_type])
        flash('Your submission has been received and is pending review.', 'success')
    except Exception as e:
        logger.error(f"Error adding item: {e}")
        flash(f'Error adding item: {e}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')