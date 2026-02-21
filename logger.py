
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    # Configure logging
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Get the root logger
    app_logger = logging.getLogger()
    app_logger.setLevel(logging.INFO)

    # Check if running in serverless environment (Vercel)
    is_serverless = os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME')
    
    if is_serverless:
        # In serverless, use StreamHandler to log to stdout (visible in Vercel logs)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.INFO)
        
        if not app_logger.handlers:
            app_logger.addHandler(console_handler)
    else:
        # Local development: use file logging
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        log_file = 'logs/app.log'
        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 5, backupCount=2)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(logging.INFO)
        
        if not app_logger.handlers:
            app_logger.addHandler(file_handler)

    return app_logger
