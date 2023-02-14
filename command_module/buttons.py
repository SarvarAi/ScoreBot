from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3


class Buttons:
    """
    This class is universal for constructing two types of buttons such as
    ReportButtons and InlineButtons.
    """

    def __init__(self, row_width_inline=None, row_width_reply=None):
        """
        Creating all markups for buttons, such as InlineKeyboardMarkup and ReplyKeyboardMarkup.
        And also additional List for storing all buttons
        :param row_width_inline: Asking a number of rows InlineButtons
        :param row_width_reply: Asking a number of rows ReportButtons
        """
        self.InMarkup = InlineKeyboardMarkup(row_width=row_width_inline)
        self.ReMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width_reply)
        self.buttons = []

    def make_inline(self, btns):
        """
        This method of the Buttons class is used to create InlineButtons
        :param btns: This is dictionary where programmer provide information about the buttons.
        key is name of buttons, value is call data
        :return:
        """
        for btn, data in btns.items():
            self.buttons.append(InlineKeyboardButton(text=btn, callback_data=data))

        return self.InMarkup.add(*self.buttons)

    def make_reply(self, btns):
        for btn, data in btns.items():
            self.buttons.append(KeyboardButton(text=btn))

        return self.ReMarkup.add(*self.buttons)
