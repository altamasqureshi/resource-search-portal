# Driver Search App

A Flask-based web application for searching printer drivers and information links, integrated with Google Sheets for dynamic data management.

## Features

- **Fuzzy Search**: Smart search using fuzzy matching to find drivers and info links
- **Google Sheets Integration**: Data stored and managed in Google Sheets
- **Real-time Updates**: Automatic data reload every 24 hours
- **User Submissions**: Users can submit new drivers/links for review
- **Responsive UI**: Clean, user-friendly interface

## Tech Stack

- **Backend**: Flask (Python)
- **Search**: FuzzyWuzzy for intelligent matching
- **Database**: Google Sheets API
- **Deployment**: Vercel (serverless)
- **Scheduling**: APScheduler / Vercel Cron Jobs

## Project Structure

```
driver_search_app/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── sheets_helper.py            # Google Sheets integration
├── logger.py                   # Logging configuration
├── requirements.txt            # Python dependencies
├── vercel.json                 # Vercel deployment config
├── templates/
│   └── index.html             # Frontend template
├── logs/                       # Application logs
└── credentials.json           # Google service account (not in repo)
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Google Cloud service account with Sheets API access
- Vercel account (for deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/driver-search-app.git
   cd driver-search-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Sheets**
   - Follow instructions in `GOOGLE_SHEETS_SETUP.md`
   - Place your `credentials.json` in the project root

4. **Configure settings**
   - Update `config.py` with your spreadsheet IDs

5. **Run the application**
   ```bash
   python app.py
   ```
   
   Visit: http://localhost:5000

### Deployment to Vercel

See detailed guides:
- **Quick Start**: `QUICK_START_VERCEL.md`
- **Full Documentation**: `VERCEL_DEPLOYMENT.md`
- **Checklist**: `DEPLOYMENT_CHECKLIST.md`

**Quick Deploy:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Add environment variables
vercel env add GOOGLE_CREDENTIALS
vercel env add SECRET_KEY

# Deploy to production
vercel --prod
```

## Environment Variables

Required for Vercel deployment:

- `SECRET_KEY`: Flask secret key for sessions
- `GOOGLE_CREDENTIALS`: Contents of credentials.json file

## Google Sheets Structure

Your spreadsheet should have three sheets:

1. **drivers**: Columns: `Model No`, `Driver download Link`
2. **info_links**: Columns: `Name`, `Link`, `Type`
3. **new_submissions**: Columns: `Timestamp`, `IP Address`, `Item Name`, `Item Link`, `Item Type`

## API Endpoints

- `GET /` - Homepage with search
- `POST /` - Search submission
- `POST /submit` - New item submission
- `GET /api/reload-data` - Reload data from Google Sheets (Cron job)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- FuzzyWuzzy for fuzzy string matching
- Google Sheets API for data management
- Vercel for serverless hosting
