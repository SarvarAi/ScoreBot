import os

from aiogram.types import Message, ReplyKeyboardRemove

from data.Bot_data.loader_unit import dp
from data.Bot_data.botdatabase import GettingTableBot
from data.user_data.database import GettingInfoFromUsers, InsertingInfoIntoUsers
from .buttons import Buttons
from .Report.report import report

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


main = {
    '🛠SOCIE': 'socie',
    '🚫SBL': 'sbl',
    '🚫SOL': 'sol',
    'FAQ': 'faq',
    '📒История': 'history'
}


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    """
    START начало бота
    Проверка пользователя на наличие в базе данных
    :param message:
    :return:
    """
    user_id = message.from_user.id
    checking_is_user_in_database = GettingInfoFromUsers().get_all_information_by_message_id(user_id=user_id)

    InsertingInfoIntoUsers().all_starts_of_users(message=message)

    if not checking_is_user_in_database:
        InsertingInfoIntoUsers().inserting_new_unique_users(message=message)

    with open('D:\Python\inha_score\data\Bot_data\Image\Welcome.jpg', mode='rb') as img:
        await message.answer_photo(img,
                                   caption='Выберите свой факультет!',
                                   reply_markup=Buttons(row_width_inline=3).make_inline(btns=main))


# ABOUT Про бота
@dp.message_handler(commands=['about'])
async def command_about(message: Message):
    await message.answer(GettingTableBot().get_message_by_description('about_bot', 'about_bot'),
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['report'])
async def command_report(message: Message):
    await report(message)
