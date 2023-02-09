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


class CreatingTableBot(Botdatabase):
    def __init__(self):
        super().__init__()

    def create_table_about_bot(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS about_bot (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        message TEXT NOT NULL
        );''')
        self.close()

    def create_table_for_freq_questions(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS freq_questions (
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
        );
        ''')
        self.close()

    def create_table_for_main_menu(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS main_menu (
        main_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
        );
        ''')
        self.commit()
        self.close()


class InsertingTableBot(Botdatabase):
    def __init__(self):
        super().__init__()
        self.columns = []
        self.information = []
        self.secret = []

    def insert(self, table, ins):
        for k, v in ins.items():
            self.columns.append(k)
            self.secret.append('?')
            self.information.append(v)

        self.cursor.execute(f'''INSERT INTO {table} ({', '.join(self.columns)}) VALUES
            ({', '.join(self.secret)})''', tuple(self.information))

        self.commit()
        self.close()


class GettingTableBot(Botdatabase):
    def __init__(self):
        super().__init__()

    def get_message_by_description(self, table_name, description):
        self.cursor.execute(f'''SELECT message FROM {table_name}
         WHERE description = ?''', (description,))
        result = self.cursor.fetchone()
        self.close()
        return result[0]


create = CreatingTableBot()
insert = InsertingTableBot()
#
# info = {
#     'description': 'Выберите свой факультет!'
# }
#
# insert.insert('main_menu', info)
# create.create_table_for_main_menu()
