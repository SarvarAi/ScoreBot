from data.Bot_data.loader_unit import dp

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .report_buttons import ReportButtuns


class Report(StatesGroup):
    theme = State()


async def report(message: Message):
    await message.answer('Вы можете задать свой вопрос или посмотерть уже на отвеченные ', reply_markup=ReportButtuns().choose_type_of_question())
    await Report.theme.set()
