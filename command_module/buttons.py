from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

report_index = 0


class Buttons:
    """
    Класс кнопок для факультетов SOCIE, SOL, SBL также FAQ
    где пользователь может задать свой вопрос или выбрать вопрос
    """

    def __init__(self):
        self.markup = InlineKeyboardMarkup(row_width=3)

    def faculty_buttons(self):
        btn = [
            InlineKeyboardButton(text='🛠SOCIE', callback_data='socie'),
            InlineKeyboardButton(text='🚫SBL', callback_data='sbl'),
            InlineKeyboardButton(text='🚫SOL', callback_data='sol'),
            InlineKeyboardButton(text='FAQ', callback_data='faq')
        ]

        return self.markup.add(*btn)


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
