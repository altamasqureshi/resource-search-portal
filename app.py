import csv
from flask import Flask, render_template, request, redirect, url_for, flash
from fuzzywuzzy import fuzz
from datetime import datetime
from fuzzywuzzy import fuzz

from logger import setup_logging

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' # Replace with a strong, random key in production

logger = setup_logging()

def search_items(query):
    results = []
    # Search in drivers.csv
    with open('drivers.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            item_name = row[0]
            if fuzz.partial_ratio(query.lower(), item_name.lower()) >= 70:
                results.append({'name': row[0], 'link': row[1], 'type': 'Printer Driver'})

    # Search in info_links.csv
    with open('info_links.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            item_name = row[0]
            if fuzz.partial_ratio(query.lower(), item_name.lower()) >= 70:
                results.append({'name': row[0], 'link': row[1], 'type': row[2]})
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