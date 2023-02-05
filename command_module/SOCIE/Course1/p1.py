from data.Bot_data.loader_unit import dp
from aiogram.types import Message, ReplyKeyboardRemove
from command_module.buttons import Messages
from command_module.SOCIE import sociebtn
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class P1_mem(StatesGroup):
    main = State()
    hw_ass_att = State()
    midScore = State()
    finScore = State()
    total = State()


@dp.message_handler(regexp='✅Physics 1', state=None)
async def sc1p1(message: Message):
    await message.answer('Давайте рассчитаем ваш Total❗')
    with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\P1grade.png', mode='rb') as img:
        await message.answer_photo(img,
                                   caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                   reply_markup=sociebtn.Buttons.start())
    await P1_mem.main.set()


@dp.message_handler(state=P1_mem.main)
async def p1_main(message: Message):
    await message.answer('''Сколько вы получила за Midterm из 30?''', reply_markup=ReplyKeyboardRemove())
    await P1_mem.midScore.set()


@dp.message_handler(state=P1_mem.midScore)
async def mid_score(message: Message, state: FSMContext):
    try:
        mid = float(message.text)
        if mid < 0 or mid > 30:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['midScore'] = mid
            await message.answer('Сколько вы получила за Final из 40?')
            await P1_mem.finScore.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=P1_mem.finScore)
async def fin_score(message: Message, state: FSMContext):
    try:
        fin = float(message.text)
        if fin < 0 or fin > 40:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['finScore'] = fin
            with open('D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\PEgrade_spc.png',
                      mode='rb') as img:
                await message.answer_photo(img,
                                           caption='''Из-за специфики описания этого раздела 🧐 \nНа сколько вы выполняли все эти требования из 20?''')
            await P1_mem.hw_ass_att.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=P1_mem.hw_ass_att)
async def imp_3_att(message: Message, state: FSMContext):
    try:
        aha = float(message.text)
        if aha < 0 or aha > 20:
            await Messages(message).error_number()
        else:
            async with state.proxy() as data:
                data['hw_ass_att'] = aha
            await message.answer('Мы высчитали ваш Total', reply_markup=sociebtn.Buttons.show())
            await P1_mem.total.set()
    except:
        await Messages(message).error_char()


@dp.message_handler(state=P1_mem.total)
async def total(message: Message, state: FSMContext):
    data = await state.get_data()

    aha = data['hw_ass_att']
    fin = data['finScore']
    mid = data['midScore']

    fin_t = (fin * 100) / 40
    fin_t_1 = (50 * fin_t) / 100
    total_t = aha + mid + fin_t_1

    await message.answer(parse_mode='HTML', text=f'<b>Ваш Total: {round(total_t, 1)}</b> 🤯',
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
