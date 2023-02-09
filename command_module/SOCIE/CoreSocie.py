from data.Bot_data.loader_unit import dp, bot
from command_module.buttons import Buttons

from aiogram.types import CallbackQuery

socie = {
    '🛠1 Курс 🧒': 'course_1_socie',
    '🚫2 Курс 👦': 'course_2_socie',
    '🚫3 Курс 👨': 'course_3_socie',
    '🚫4 Курс 👱‍♂': 'course_4_socie',
    '🔙Назад': 'back_course'
}

main = {
    '🛠SOCIE': 'socie',
    '🚫SBL': 'sbl',
    '🚫SOL': 'sol',
    'FAQ': 'faq',
    '📒История': 'history'
}


@dp.callback_query_handler(lambda call: 'socie' in call.data)
async def faculty_socie(call: CallbackQuery):
    message_id = call.message.message_id
    chat_id = call.message.chat.id

    await bot.edit_message_caption(chat_id=chat_id,
                                   message_id=message_id,
                                   caption='Выберите курс',
                                   reply_markup=Buttons(row_width_inline=2).make_inline(btns=socie))


@dp.callback_query_handler(lambda call: 'back_course' in call.data)
async def faculty_socie_back(call: CallbackQuery):
    message_id = call.message.message_id
    chat_id = call.message.chat.id

    await bot.edit_message_caption(chat_id=chat_id,
                                   message_id=message_id,
                                   caption='Выберите свой факультет!',
                                   reply_markup=Buttons(row_width_inline=3).make_inline(btns=main))
