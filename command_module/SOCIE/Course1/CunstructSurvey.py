from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup


class StartSurvey:
    def __init__(self, subject_states):
        self.State = subject_states

    async def start_survey(self, text, message, mystate, path_photo):
        await message.answer(text=text)
        with open(f'D:\Python\inha_score\data_module\Bot_data\Image\SOCIE\Course1\{path_photo}.png', mode='rb') as img:
            await message.answer_photo(img,
                                       caption='Сейчас будем считать ваш балл по этой таблице давайте начнем\n♦Вводите все числа без знака процент (%)',
                                       )
        await self.State.mystate.set()
