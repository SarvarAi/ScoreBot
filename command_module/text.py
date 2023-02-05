from aiogram.types import Message
from . import default_structures as ds
from data_module.Bot_data.loader_unit import dp

@dp.message_handler(content_types=['text'])
async def react_text(message: Message):
    if ds.report_index > 0:
        await message.answer('✅Ваше сообщение успешно отправленно')
        ds.Database().report_data(message)
        ds.report_index = 0
    else:
        print(f'user: {message.chat.id}, report_index: {ds.report_index}, text: {message.text}')

