import os

from aiogram.types import Message, ReplyKeyboardRemove

from data.Bot_data.loader_unit import dp
from data.Bot_data.botdatabase import GettingTableBot
from data.user_data.database import GettingInfoFromUsers, InsertingInfoIntoUsers
from .buttons import Buttons

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

main = {
    '🛠SOCIE': 'socie',
    '🚫SBL': 'sbl',
    '🚫SOL': 'sol',
    '🚫CSE': 'cse',
    'FAQ': 'faq',
    '📒История': 'history'
}


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    """
    START Beginning of the bot where user is simultaneously registrating user to the database.
    In order to know number of unique users in the database.
    User Doesn't see any operations of registrating
    :param message: message
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
                                   reply_markup=Buttons(row_width_inline=2).make_inline(btns=main))


@dp.message_handler(commands=['about'])
async def command_about(message: Message):
    """
    ABOUT is special command where user can see special information about bot.
    The owner of this bot can post any information that he/she wants
    :param message: message
    :return:
    """
    await message.answer(GettingTableBot().get_message_by_description('about_bot', 'about_bot'),
                         reply_markup=ReplyKeyboardRemove())

