from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
import sqlite3

report_index = 0

about = '''
🧑‍🎓Этот бот был создан студентом ИНХА
🥷Создатель желает остоваться анонимным
📈Этот бот развивается день ото дня, добавляя новые функции
📩Если вы хотите отправить сообщение создателю, выберите в меню /report
📝Автор создал этого бота, чтобы помочь учащимся рассчитать баллы по любому предмету.
🐍Бот написан на Python и на самом мощном библиотеке для телеграмма aiogram
'''


class Database:
    # creating a text file with the whole information types 'text' and callbacks
    @staticmethod
    def start_data(message: Message):
        database = sqlite3.connect(r"D:\Python\inha_score\data_module\user_data\data_base.db")
        cursor = database.cursor()

        msg_id = message.message_id
        user_id = message.from_user.id
        bot_ask = message.from_user.is_bot
        first_name = message.from_user.first_name
        user_name = message.from_user.username
        langc = message.from_user.language_code
        tp = message.chat.type
        datetg = message.date

        cursor.execute('''
                INSERT INTO start(message_id, user_id, is_bot, first_name, username, language_code , type, date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                ''', (msg_id, user_id, bot_ask, first_name, user_name, langc, tp, datetg))

        print(f'user_id: {user_id}, data_base: start')
        database.commit()
        database.close()

    @staticmethod
    def report_data(message: Message):
        database = sqlite3.connect(r"D:\Python\inha_score\data_module\user_data\data_base.db")
        cursor = database.cursor()

        msg_id = message.message_id
        user_id = message.from_user.id
        bot_ask = message.from_user.is_bot
        first_name = message.from_user.first_name
        user_name = message.from_user.username
        langc = message.from_user.language_code
        tp = message.chat.type
        datetg = message.date
        text = message.text

        cursor.execute('''
        INSERT INTO reports(message_id, user_id, is_bot, first_name, username, language_code , type, date, text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (msg_id, user_id, bot_ask, first_name, user_name, langc, tp, datetg, text))

        print(f'user_id: {user_id}, data_base: reports')
        database.commit()
        database.close()


class Buttons:

    def faculty(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        socie = KeyboardButton('🛠SOCIE')
        sbl = KeyboardButton('🚫SBL')
        sol = KeyboardButton('🚫SOL')
        return markup.add(socie, sbl, sol)


class Messages:
    def __init__(self, message=None):
        self.message = message

    async def error_number(self):
        return await self.message.reply('🚫Вы ввели неправильное число 😕Введите еще раз')

    async def error_char(self):
        return await self.message.reply('🚫Вы ввели нe корректно 😟Введите еще раз')

    @staticmethod
    async def not_ready(message: Message):
        await message.answer(parse_mode='HTML', text=
        f'Нам очень жаль, но пока что мы не дороботали <b>{message.text[1:]}</b> 😢, наши программисты на данный момент работают над этим🧑‍💻')
