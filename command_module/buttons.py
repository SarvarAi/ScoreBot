from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

report_index = 0


class Buttons:
    """
    Кнопки для курса
    """

    def __init__(self, row_width_inline=None, row_width_reply=None):
        self.InMarkup = InlineKeyboardMarkup(row_width=row_width_inline)
        self.ReMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width_reply)
        self.buttons = []

    def make_inline(self, btns):
        for btn, data in btns.items():
            self.buttons.append(InlineKeyboardButton(text=btn, callback_data=data))

        print(self.buttons)
        return self.InMarkup.add(*self.buttons)

    def make_reply(self, btns):
        for btn, data in btns.items():
            self.buttons.append(KeyboardButton(text=btn))

        return self.ReMarkup.add(*self.buttons)
