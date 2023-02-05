from data.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.buttons import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class C1_memory(StatesGroup):
    main = State()
    attendance = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()


@dp.message_handler(regexp='✅Calculus 1', state=None)
async def sc1c1(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\С1grade.png', mode='rb') as img:
        await message.answer_photo(img, caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await C1_memory.main.set()


@dp.message_handler(state=C1_memory.main)
async def c1_main(message: Message):
    await message.answer('''Как вы думете примерно сколько процетов лекций вы посещали?''', reply_markup=ReplyKeyboardRemove())
    await C1_memory.attendance.set()


@dp.message_handler(state=C1_memory.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att > 100 or att < 0:
            await Messages(message).error_number()
        else:
            await message.answer('В среднем на сколько поинтов хорошо из 100 вы писали Assigments')
            async with state.proxy() as data:
                data['attendance'] = att
            await C1_memory.assignments.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=C1_memory.assignments)
async def assigments(message: Message, state: FSMContext):
    try:
        ass = float(message.text)
        if ass > 100 or ass < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Cколько вы получили за Midterm из 100')
            async with state.proxy() as data:
                data['assignments'] = ass
            await C1_memory.midScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=C1_memory.midScore)
async def midmessage(message: Message, state: FSMContext):
    try:
        midm = float(message.text)
        if midm > 100 or midm < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Cколько вы получили за Final из 100')
            async with state.proxy() as data:
                data['midScore'] = midm
            await C1_memory.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=C1_memory.finScore)
async def fin(message: Message, state: FSMContext):
    try:
        finm = float(message.text)
        if finm > 100 or finm < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            async with state.proxy() as data:
                data['finScore'] = finm
            await C1_memory.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=C1_memory.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    ass = data['assignments']
    finm = data['finScore']
    midm = data['midScore']

    att_t = (10 * att) / 100
    ass_t = (30 * ass) / 100
    fin_t = (30 * finm) / 100
    mid_t = (30 * midm) / 100

    total_m = att_t + ass_t + fin_t + mid_t
    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total_m, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
