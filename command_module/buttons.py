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
            InlineKeyboardButton(text='FAQ', callback_data='faq'),
            InlineKeyboardButton(text='📒История', callback_data='history')
        ]

        return self.markup.add(*btn)


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
