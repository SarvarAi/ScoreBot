import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Botdatabase:
    """
    Этот класс служит для создания, добовления и выввода информации связанного с ботом.
    """

    def __init__(self):
        self.database_path = os.path.join(BASE_DIR, 'botdatabase.db')
        self.database = sqlite3.connect(self.database_path)
        self.cursor = self.database.cursor()
        self.commit = self.database.commit
        self.close = self.database.close

    def create_table_about_bot(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS about_bot (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        message TEXT NOT NULL
        );''')
        self.close()

    def inserting_information(self, table_name, description, message):
        self.cursor.execute(f'''INSERT INTO {table_name} (description, message) VALUES 
        (?, ?);
        ''', (description, message))
        self.commit()
        self.close()

    def get_message_by_description(self, table_name, description):
        self.cursor.execute(f'''SELECT message FROM {table_name}
         WHERE description = ?''', (description,))
        result = self.cursor.fetchone()
        self.close()
        return result[0]


print()
