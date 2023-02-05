# - *- coding : utf-8 - *-

from aiogram import executor
from data_module.Bot_data.loader_unit import dp

import command_module

if __name__ == '__main__':
    executor.start_polling(dp)
