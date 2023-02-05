from data_module.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.default_structures import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Ae_mem(StatesGroup):
    main = State()
    attendance = State()
    discussion = State()
    quiz = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()


@dp.message_handler(regexp='✅Academic English 1', state=None)
async def sc1ae(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\AE1grade.png', mode='rb') as img:
        await message.answer_photo(photo=img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await Ae_mem.main.set()


@dp.message_handler(state=Ae_mem.main)
async def ae_main(message: Message):
    await message.answer('''Как вы думете примерно сколько процетов лекций вы посещали?''',
                         reply_markup=ReplyKeyboardRemove())
    await Ae_mem.attendance.set()


@dp.message_handler(state=Ae_mem.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att > 100 or att < 0:
            await Messages(message).error_number()
        else:
            await message.answer(
                'Сколько в среднем из 10, ваша учительница оценивала вашу активность на уроке?')
            async with state.proxy() as data:
                data['attendance'] = att
            await Ae_mem.discussion.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.discussion)
async def discussion(message: Message, state: FSMContext):
    try:
        dis = float(message.text)
        if dis > 10 or dis < 0:
            await Messages(message).error_number()
        else:
            await message.answer('На сколько процентов в среднем вы хорошо писали Quiz')
            async with state.proxy() as data:
                data['discussion'] = dis
            await Ae_mem.quiz.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.quiz)
async def quiz(message: Message, state: FSMContext):
    try:
        quiz = float(message.text)
        if quiz > 100 or quiz < 0:
            await Messages(message).error_number()
        else:
            await message.answer(
                'Как вы думаете сколько ваша учительиница поставила из 100 за ваши assigments за семестр? ')
            async with state.proxy() as data:
                data['quiz'] = quiz
            await Ae_mem.assignments.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.assignments)
async def assigments(message: Message, state: FSMContext):
    try:
        ass = float(message.text)
        if ass > 100 or ass < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Cколько вы получили за Midterm из 66')
            async with state.proxy() as data:
                data['assignments'] = ass
            await Ae_mem.midScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.midScore)
async def mid(message: Message, state: FSMContext):
    try:
        midm = float(message.text)
        if midm > 66 or midm < 0:
            await Messages(message).error_number()
        else:
            await message.answer('Cколько вы получили за Final из 58')
            async with state.proxy() as data:
                data['midScore'] = midm
            await Ae_mem.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.finScore)
async def fin(message: Message, state: FSMContext):
    try:
        finm = float(message.text)
        if finm > 58 or finm < 0:
            await Messages(message).error_number()
        else:
            await message.answer(
                'Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            async with state.proxy() as data:
                data['finScore'] = finm
            await Ae_mem.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Ae_mem.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    dis = data['discussion']
    quiz = data['quiz']
    ass = data['assignments']
    midm = data['midScore']
    finm = data['finScore']

    att_t = (10 * att) / 100
    quiz_t = (10 * quiz) / 100
    ass_t = (10 * ass) / 100
    midm_1 = (midm * 100) / 66
    midm_t = (midm_1 * 25) / 100
    finm_1 = (finm * 100) / 58
    finm_t = (finm_1 * 25) / 100

    total_m = att_t + quiz_t + dis + midm_t + finm_t + ass_t
    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total_m, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
