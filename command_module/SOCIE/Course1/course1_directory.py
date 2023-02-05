from aiogram.types import Message
from command_module.SOCIE import sociebtn
from command_module import buttons as ds
from data.Bot_data.loader_unit import dp


@dp.message_handler(regexp='🛠1 Курс 🧒')
async def course1(message: Message):
    await message.answer('Выберите урок', reply_markup=sociebtn.Buttons.course1_but())

# переделать так как он внутри первого курса отлавливает 2, 3, 4 курсы
@dp.message_handler(regexp='🚫2 Курс 👦')
async def course2(message: Message):
    await ds.Messages.not_ready(message)


@dp.message_handler(regexp='🚫3 Курс 👨')
async def course2(message: Message):
    await ds.Messages.not_ready(message)


@dp.message_handler(regexp='🚫4 Курс 👱‍♂')
async def course2(message: Message):
    await ds.Messages.not_ready(message)
