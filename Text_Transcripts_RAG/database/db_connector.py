import mysql.connector
import os
import sys
from dotenv import load_dotenv
from Text_Transcripts_RAG.exception import QnAException
from Text_Transcripts_RAG.logger import logging

load_dotenv()
logging.info("Loaded the environment variables")


class DBConnector:
    def __init__(self):
        logging.info("Initiated the database connection configuration\n")
        try:
            self.mydb = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                host=os.getenv("DB_HOST"),
                password=os.getenv("DB_PASSWORD")
            )
            logging.info("Successfully connected to the database")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            raise QnAException(err, sys)

    def create_database(self):
        try:
            logging.info("Creating the database\n")
            conn = self.mydb.cursor()
            conn.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
            logging.info(f"Database {os.getenv('DB_NAME')} created successfully\n")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            raise QnAException(err, sys)
        finally:
            conn.close()

    def create_table(self):
        try:
            logging.info("Creating the table..\n")
            conn = self.mydb.cursor()
            conn.execute(f"USE {os.getenv('DB_NAME')};")
            logging.info(f"Using the database {os.getenv('DB_NAME')}\n")

            # Check if the table exists
            conn.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = %s AND table_name = %s
            """, (os.getenv('DB_NAME'), os.getenv("ETECH_TEXT_TABLE")))

            table_exists = conn.fetchone()[0]

            logging.info(f"Table exists: {table_exists}\n")

            conn.execute(f"show tables;")
            table_lists = conn.fetchall()

            logging.info(f"Tables in the database: {table_lists}\n")
            # table_names = [table_list[0] for table_list in table_lists]

            table_names = []
            for table in table_lists:
                logging.info(f"Table name: {table[0]}\n")
                table_names.append(table[0])

            logging.info(f"Table names: {table_names}")

            if os.getenv("TABLE_NAME") not in table_names:
                logging.info("Table is not present, creating the table\n")
                query = f"""
                CREATE TABLE {os.getenv("TABLE_NAME")} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                session_id VARCHAR(255),
                file_name VARCHAR(255),
                file_content TEXT,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
                conn.execute(query)
                logging.info("Table created successfully\n")
            else:
                logging.info("Table already exists\n")

        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            raise QnAException(err, sys)

        finally:
            logging.info("Closing the connection\n")
            conn.close()
            self.mydb.close()


if __name__ == '__main__':
    db = DBConnector()
    db.create_database()
    db.create_table()
