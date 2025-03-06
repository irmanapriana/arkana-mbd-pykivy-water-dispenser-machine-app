import logging
from datetime import datetime
import os

class ActivityLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.update_log_file()
    
    def update_log_file(self):
        log_filename = datetime.now().strftime("%Y-%m-%d.log")
        log_path = os.path.join(self.log_dir, log_filename)
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def log_activity(self, activity):
        self.update_log_file()  # Ensure log file is updated daily
        logging.info(activity)

if __name__ == "__main__":
    logger = ActivityLogger()
    logger.log_activity("User started the application.")
    logger.log_activity("User clicked on button X.")
    logger.log_activity("User closed the application.")
