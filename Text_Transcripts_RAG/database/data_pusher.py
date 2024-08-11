from Text_Transcripts_RAG.database.db_connector import DBConnector
from Text_Transcripts_RAG.logger import logging
from Text_Transcripts_RAG.exception import QnAException
import os
import sys
import mysql.connector

logging.info("Initiated the data pusher configuration\n")


class DataPusher:
    def __init__(self):
        logging.info("Initiated the data pusher configuration and calling the DB Connector Components\n")
        self.db_connector = DBConnector()
        self.db_connector.create_database()
        self.db_connector.create_table()
        logging.info("Successfully created the database and table\n")

    def inserting_text_file(self, session_id: int, file_name: str, file_path: str):
        try:
            logging.info("Inserting the text file into the database\n")
            conn = self.db_connector.mydb.cursor()

            conn.execute(f"USE {os.getenv('DB_NAME')};")
            logging.info(f"Using the database {os.getenv('DB_NAME')}\n")

            conn.execute(f"INSERT INTO {os.getenv('ETECH_TEXT_TABLE')} (text_file) VALUES ({file_path});")
            logging.info("Successfully inserted the text file into the database\n")

        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            raise QnAException(err, sys)
        finally:
            conn.close()

