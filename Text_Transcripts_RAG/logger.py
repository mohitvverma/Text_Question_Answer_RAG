import logging
from datetime import datetime
import os
import sys


LOG_FILE_NAME = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# os.makedirs('logs', exist_ok=True)

main_file_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.insert(0, main_file_path)

LOG_PATH = os.path.join(main_file_path, 'Logs_data', LOG_FILE_NAME)

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE_NAME)

LOG_FORMAT = '%(asctime)s  %(filename)s  %(lineno)d - %(levelname)s - %(message)s'

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=LOG_FORMAT,
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('This is a test log message')
