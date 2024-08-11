import logging
from datetime import datetime
import os
import sys
from Text_Transcripts_RAG.constants import MAIN_FILE_PATH


LOG_FILE_NAME = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

main_file_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.insert(0, MAIN_FILE_PATH)

LOG_PATH = os.path.join(MAIN_FILE_PATH, 'Logs_data', LOG_FILE_NAME)
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
