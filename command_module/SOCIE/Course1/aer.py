from data.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.buttons import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





@dp.message_handler(regexp='✅Academic English Reading')
async def sc1aer(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\AERgrade.png', mode='rb') as img:
        await message.answer_photo(photo=img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)\n♦Бот автоматически берет 10 из 10 Assignments',
                                   reply_markup=sociebtn.Buttons.start())
    await Aer_mem.main.set()


@dp.message_handler(state=Aer_mem.main)
async def main_it(message: Message):
    await message.answer('''Как вы думете примерно сколько процетов лекций вы посещали?''',
                         reply_markup=ReplyKeyboardRemove())
    await Aer_mem.attendance.set()


@dp.message_handler(state=Aer_mem.attendance)
async def attendance(message: Message, state: FSMContext):
    try:
        att = float(message.text)
        if att < 0 or att > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['attendance'] = att
            await message.answer('На сколько процентов в среднем вы хорошо писали Quiz?')
            await Aer_mem.quiz.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Aer_mem.quiz)
async def quiz(message: Message, state: FSMContext):
    try:
        q = float(message.text)
        if q < 0 or q > 100:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['quiz'] = q
            await message.answer('На сколько баллов из 42 вы написали Midterm?')
            await Aer_mem.midScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Aer_mem.midScore)
async def mid_exam(message: Message, state: FSMContext):
    try:
        mid = float(message.text)
        if mid < 0 or mid > 42:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['midScore'] = mid
            await message.answer('На сколько баллов из 71 вы написали Final?')
            await Aer_mem.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Aer_mem.finScore)
async def final_exam(message: Message, state: FSMContext):
    try:
        fin = float(message.text)
        if fin < 0 or fin > 71:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['finScore'] = fin
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            await Aer_mem.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=Aer_mem.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    att = data['attendance']
    q = data['quiz']
    mid = data['midScore']
    fin = data['finScore']

    att_t = (10 * att) / 100
    q_t = (20 * q) / 100
    mid_t = (100 * mid) / 42
    mid_t_1 = (30 * mid_t) / 100
    fin_t = (100 * fin)/ 71
    fin_t_1 = (30 * fin_t)/ 100

    total = att_t + q_t + mid_t_1 + fin_t_1

    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())

    await state.finish()
