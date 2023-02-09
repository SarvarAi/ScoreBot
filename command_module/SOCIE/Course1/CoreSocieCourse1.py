from aiogram.types import CallbackQuery

from data.Bot_data.loader_unit import dp, bot
from command_module.buttons import Buttons

choose = {
    'AE1': 'ae1',
    'AER': 'aer1',
    'C1': 'c1',
    'P1': 'p1',
    'PE1': 'pe1',
    'IT': 'intro1',
    'OOP1': 'oop1',
    '🔙': 'back_course'
}


@dp.callback_query_handler(lambda call: 'course_1_socie' in call.data)
async def core_socie_course_1(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    await bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_id,
        caption='Выберите предмет',
        reply_markup=Buttons(row_width_inline=4).make_inline(btns=choose))
