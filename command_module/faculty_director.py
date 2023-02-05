from data.Bot_data.loader_unit import dp
from aiogram.types import Message
from command_module.SOCIE import sociebtn
from command_module import buttons as ds


@dp.message_handler(regexp='🛠SOCIE')
async def faculty_socie(message: Message):
    await message.answer(text='Выберите курс', reply_markup=sociebtn.Buttons.courses())



@dp.message_handler(regexp='🚫SBL')
async def faculty_sbl(message: Message):
    await ds.Messages.not_ready(message)


@dp.message_handler(regexp='🚫SOL')
async def faculty_sbl(message: Message):
    await ds.Messages.not_ready(message)










