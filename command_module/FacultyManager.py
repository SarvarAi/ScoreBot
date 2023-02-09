from data.Bot_data.loader_unit import dp, bot
from aiogram.types import Message, CallbackQuery
from command_module.SOCIE import sociebtn
from command_module.buttons import Buttons
from .SOCIE.sociebtn import SocieButtons

socie = {
    '🛠1 Курс 🧒': 'course_1_socie',
    '🚫2 Курс 👦': 'course_2_socie',
    '🚫3 Курс 👨': 'course_3_socie',
    '🚫4 Курс 👱‍♂': 'course_4_socie',
    '🔙Назад': 'back_course'
}


@dp.callback_query_handler(lambda call: 'socie' in call.data)
async def faculty_socie(call: CallbackQuery):
    message_id = call.message.message_id
    chat_id = call.message.chat.id

    await bot.edit_message_caption(chat_id=chat_id,
                                   message_id=message_id,
                                   caption='Выберите курс',
                                   reply_markup=SocieButtons(row_width_inline=2).make_inline(btns=socie))


@dp.callback_query_handler(lambda call: 'back_course' in call.data)
async def faculty_socie_back(call: CallbackQuery):
    message_id = call.message.message_id
    chat_id = call.message.chat.id

    await bot.edit_message_caption(chat_id=chat_id,
                                   message_id=message_id,
                                   caption='Выберите свой факультет!',
                                   reply_markup=Buttons().faculty_buttons())


# @dp.message_handler(regexp='🚫SBL')
# async def faculty_sbl(message: Message):
#     await ds.Messages.not_ready(message)
#
#
# @dp.message_handler(regexp='🚫SOL')
# async def faculty_sbl(message: Message):
#     await ds.Messages.not_ready(message)
