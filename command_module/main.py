from data_module.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from . import default_structures as ds


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    ds.Database.start_data(message)
    with open('D:\Python\inha_score\data_module\Bot_data\Image\Welcome.jpg', mode='rb') as img:
        await message.answer_photo(img, parse_mode='HTML',
                                   caption='Выберите свой факультет! (обращайтесь создателю через /report)',
                                   reply_markup=ds.Buttons().faculty())


@dp.message_handler(commands=['about'])
async def command_about(message: Message):
    await message.answer(ds.about, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['report'])
async def command_report(messaage: Message):
    await messaage.answer('❗Введите Сообщение❗', reply_markup=ReplyKeyboardRemove())
    ds.report_index += 1
