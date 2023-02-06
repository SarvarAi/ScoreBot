from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class ReportButtuns:
    def __init__(self):
        self.Replymarkup = ReplyKeyboardMarkup(resize_keyboard=True)
        self.Inlinemarkup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    def choose_type_of_question(self):
        return self.Inlinemarkup.add(*[
            InlineKeyboardButton(text='Отвеченные вопросы✅', callback_data='fast_question'),
            InlineKeyboardButton(text='Задать свой🤨', callback_data='my_question'),
            InlineKeyboardButton(text='❌Отмена', callback_data='cancel_type')
        ])

    def choose_theme(self):
        return self.Replymarkup.add(*[
            KeyboardButton(text='Хочу стать частью проекта!'),
            KeyboardButton(text='А вы кто?'),
            KeyboardButton(text='Назад'),
            KeyboardButton(text='🔙Назад')
        ])
