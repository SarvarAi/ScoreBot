import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class CreateTable:
    def __init__(self):
        self.database_path = os.path.join(BASE_DIR, 'users.db')
        self.database = sqlite3.connect(self.database_path)
        self.cursor = self.database.cursor()
        self.commit = self.database.commit
        self.close = self.database.close

    def creating_table_of_unique_users(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users_unique (
            user_table_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_telegram_id VARCHAR(25) UNIQUE NOT NULL,
            is_bot VARCHAR(1) NOT NULL,
            first_name VARCHAR(255) NOT NULL,
            username TEXT,
            language VARCHAR(10),
            date_time DATETIME NOT NULL);
        ''')
        self.commit()
        self.close()


# CreateTable().creating_table_of_unique_users()



