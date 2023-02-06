from aiogram.dispatcher.filters.state import State, StatesGroup


class Report(StatesGroup):
    theme = State()

