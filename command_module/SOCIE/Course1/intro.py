from data.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.buttons import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





@dp.message_handler(regexp='✅Introduction to IT')
async def sc1intro(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\ITgrade.png', mode='rb') as img:
        await message.answer_photo(photo=img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await Intor_mem.main.set()


@dp.message_handler(state=Intor_mem.main)
async def main_it(message: Message):
    await message.answer('''Как вы думете примерно сколько процетов лекций вы посещали?''',
                         reply_markup=ReplyKeyboardRemove())
    await Intor_mem.attendance.set()


@dp.message_handler(state=Intor_mem.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att < 0 or att > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['attendance'] = att
            await message.answer('В среднем сколько процентов assignments вы сдали за семестр?')
            await Intor_mem.assignments.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Intor_mem.assignments)
async def assignments(message: Message, state: FSMContext):
    try:
        ass = float(message.text)
        if ass < 0 or ass > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['assignments'] = ass
            await message.answer('На сколько процентов вы хорошо писали Quiz?')
            await Intor_mem.quiz.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Intor_mem.quiz)
async def quizes(message: Message, state: FSMContext):
    try:
        q = float(message.text)
        if q < 0 or q > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['quiz'] = q
            await message.answer('На сколько баллов из 100 вы написали Midterm?')
            await Intor_mem.midScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Intor_mem.midScore)
async def midterm(message: Message, state: FSMContext):
    try:
        mid = float(message.text)
        if mid < 0 or mid > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['midScore'] = mid
            await message.answer('На сколько баллов из 100 вы написали Final?')
            await Intor_mem.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Intor_mem.finScore)
async def midterm(message: Message, state: FSMContext):
    try:
        fin = float(message.text)
        if fin < 0 or fin > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['finScore'] = fin
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            await Intor_mem.total.set()
    except:
        await Messages(message).error_char()



@dp.message_handler(state=Intor_mem.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    ass = data['assignments']
    quiz = data['quiz']
    mid = data['midScore']
    fin = data['finScore']

    att_t = (10 * att) / 100
    ass_t = (15 * ass) / 100
    quiz_t = (15 * quiz) / 100
    mid_t = (30 * mid) / 100
    fin_t = (30 * fin) / 100

    total = att_t + ass_t + quiz_t + mid_t + fin_t
    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()