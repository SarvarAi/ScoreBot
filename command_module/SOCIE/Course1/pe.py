from data.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.buttons import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





@dp.message_handler(regexp='✅Physics Experiment 1', state=None)
async def sc1pe(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\PEtableGrade.png', mode='rb') as img:
        await message.answer_photo(photo=img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await Pe_mem.main.set()


@dp.message_handler(state=Pe_mem.main)
async def main_pe(message: Message):
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\PEgrade.png', mode='rb') as img:
        await message.answer_photo(photo=img, parse_mode='HTML',
                                   caption='Как вы думете примерно сколько процентов лекций вы <b>НЕ</b> посещали?',
                                   reply_markup=ReplyKeyboardRemove())
    await Pe_mem.attendance.set()


@dp.message_handler(state=Pe_mem.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att < 0 or att > 16:
            await Messages(message).error_number()
        elif att > 3:
            await message.answer('Воу кажется у вас F (фейл) 😰')
            await state.finish()
        else:
            async with state.proxy() as data:
                data['attendance'] = att
            await message.answer('В среднем сколько баллов вы получали за Lab assignment?')
            await Pe_mem.lab.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Pe_mem.lab)
async def lab_assignment(message: Message, state: FSMContext):
    try:
        l = float(message.text)
        if l < 0 or l > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['lab'] = l
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            await Pe_mem.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Pe_mem.total)
async def total_mark(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    l = data['lab']

    l = (90 * l) / 100
    total = l + (10 - att)
    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
