from data_module.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.default_structures import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class OOP1_mem(StatesGroup):
    main = State()
    attendance = State()
    quiz = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()


@dp.message_handler(regexp='✅Object Oriented Programming 1', state=None)
async def sc1ae(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\OOP1grade.png', mode='rb') as img:
        await message.answer_photo(img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await OOP1_mem.main.set()


@dp.message_handler(state=OOP1_mem.main)
async def oop1_main(message: Message):
    await message.answer('''Как вы думете примерно сколько процетов лекций вы посещали?''',
                         reply_markup=ReplyKeyboardRemove())
    await OOP1_mem.attendance.set()


@dp.message_handler(state=OOP1_mem.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att > 100 or att < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Средний процент правильных ответов в квизах за семестр?')
            async with state.proxy() as data:
                data['attendance'] = att
            await OOP1_mem.quiz.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=OOP1_mem.quiz)
async def quizoop1(message: Message, state: FSMContext):
    try:
        quiz = float(message.text)
        if quiz > 100 or quiz < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Средний процент сданных ДЗ за семестр?')
            async with state.proxy() as data:
                data['quiz'] = quiz
            await OOP1_mem.assignments.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=OOP1_mem.assignments)
async def hwoop1(message: Message, state: FSMContext):
    try:
        hw = float(message.text)
        if hw > 100 or hw < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Сколько из 30 вы набрали в Midterm?')
            async with state.proxy() as data:
                data['assignments'] = hw
            await OOP1_mem.midScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=OOP1_mem.midScore)
async def midterm(message: Message, state: FSMContext):
    try:
        mid = float(message.text)
        if mid > 30 or mid < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Сколько из 30 вы набрали в Final?')
            async with state.proxy() as data:
                data['midScore'] = mid
            await OOP1_mem.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=OOP1_mem.finScore)
async def final(message: Message, state: FSMContext):
    try:
        fin = float(message.text)
        if fin > 30 or fin < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            async with state.proxy() as data:
                data['finScore'] = fin
            await OOP1_mem.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=OOP1_mem.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    quiz = data['quiz']
    hw = data['assignments']
    mid = data['midScore']
    fin = data['finScore']

    att_t = (5 * att) / 100
    quiz_t = (20 * quiz) / 100
    hw_t = (15 * hw) / 100
    total = att_t + quiz_t + hw_t + mid + fin
    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
