from data.Bot_data.loader_unit import dp, bot

from aiogram.types import Message, CallbackQuery
from .states_report import Report
from aiogram.dispatcher import FSMContext

from .report_buttons import ReportButtuns
from command_module.buttons import Buttons


async def report(message: Message):
    """
    Начало Report запрашивание ответа на тип вопроса
    :param message:
    :return:
    """
    await message.answer('Вы можете задать свой вопрос или посмотерть уже на отвеченные ',
                         reply_markup=ReportButtuns().choose_type_of_question())
    await Report.theme.set()


@dp.callback_query_handler(lambda call: 'cancel_type' in call.data,
                           state=Report.theme)
async def report_cancel(call: CallbackQuery, state: FSMContext):
    """
    Отмена всего Report
    :param call:
    :param state:
    :return:
    """
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    with open('D:\Python\inha_score\data\Bot_data\Image\Welcome.jpg', mode='rb') as img:
        await call.message.answer_photo(
            photo=img,
            caption='Выберите свой факультет!',
            reply_markup=Buttons().faculty_buttons()
        )
    await state.finish()
