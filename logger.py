
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure logging
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_file = 'logs/app.log'

    # Use RotatingFileHandler to limit log file size
    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 5, backupCount=2)  # 5MB per file, 2 backups
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    # Get the root logger
    app_logger = logging.getLogger()
    app_logger.setLevel(logging.INFO)

    # Add the handler to the logger
    if not app_logger.handlers:
        app_logger.addHandler(file_handler)

    return app_logger
