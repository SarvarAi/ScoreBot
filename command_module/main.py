from aiogram.types import Message, ReplyKeyboardRemove

from data.Bot_data.loader_unit import dp
from data.Bot_data.botdatabase import Botdatabase
from .buttons import Buttons


# START начало бота
@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    with open('D:\Python\inha_score\data\Bot_data\Image\Welcome.jpg', mode='rb') as img:
        await message.answer_photo(img, parse_mode='HTML',
                                   caption='Выберите свой факультет! (обращайтесь создателю через /report)',
                                   reply_markup=Buttons().faculty_buttons())


# ABOUT Про бота
@dp.message_handler(commands=['about'])
async def command_about(message: Message):
    await message.answer(Botdatabase().get_message_by_description('about_bot', 'about_bot'),
                         reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(commands=['report'])
# async def command_report(messaage: Message):
#     await messaage.answer('❗Введите Сообщение❗', reply_markup=ReplyKeyboardRemove())
#     ds.report_index += 1
