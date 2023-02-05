import sqlite3
import os.path
import datetime

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Users:
    """
    Подключение к базе данных пользователей
    """

    def __init__(self):
        self.database_path = os.path.join(BASE_DIR, 'users.db')
        self.database = sqlite3.connect(self.database_path)
        self.cursor = self.database.cursor()
        self.commit = self.database.commit
        self.close = self.database.close


class CreatingTablesUsers(Users):
    """
    Создание таблиц в базе данных пользователей
    """

    def __init__(self):
        super().__init__()

    def creating_table_of_unique_users(self):
        """
        Создание таблицы в базе данных для уникальных пользователей
        :return:
        """
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

    def creating_table_of_users_starts(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users_starts (
            user_table_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_telegram_id VARCHAR(25),
            is_bot VARCHAR(1),
            first_name VARCHAR(255),
            username TEXT,
            language VARCHAR(10),
            date_time DATETIME);
        ''')
        self.commit()
        self.close()


class InsertingInfoIntoUsers(Users):
    """
    Добавление информации в таблицы базу данных пользователей
    """

    def __init__(self):
        super().__init__()

    def inserting_new_unique_users(self, message):
        """
        Добавление нового пользователья когда он первый раз запускает бота
        :param message:
        :return:
        """
        user_telegram_id = message.from_user.id
        is_bot = message.from_user.is_bot
        first_name = message.from_user.first_name
        username = message.from_user.username
        language = message.from_user.language_code
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute(
            '''INSERT INTO users_unique (user_telegram_id, is_bot, first_name, username, language, date_time)
                VALUES (?, ?, ?, ?, ?, ?);''', (user_telegram_id, is_bot, first_name, username, language, date_time))
        self.commit()
        self.close()

    def all_starts_of_users(self, message):
        """
        Для подсчета всех стартов пользователей
        :param message:
        :return:
        """
        user_telegram_id = message.from_user.id
        is_bot = message.from_user.is_bot
        first_name = message.from_user.first_name
        username = message.from_user.username
        language = message.from_user.language_code
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute(
            '''INSERT INTO users_starts (user_telegram_id, is_bot, first_name, username, language, date_time)
                VALUES (?, ?, ?, ?, ?, ?);''', (user_telegram_id, is_bot, first_name, username, language, date_time))
        self.commit()
        self.close()


class GettingInfoFromUsers(Users):
    """
    Получение данных из таблиц пользователей
    """

    def __init__(self):
        super().__init__()

    def get_all_information_by_message_id(self, user_id):
        """
        Проверка наличия пользователя в таблице
        :param user_id:
        :return:
        """
        self.cursor.execute('''SELECT * FROM users_unique WHERE user_telegram_id =?''', (user_id,))
        result = self.cursor.fetchall()
        self.close()
        return result
