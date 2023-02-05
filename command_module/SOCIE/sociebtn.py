from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Buttons:
    @staticmethod
    def courses():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        c1 = KeyboardButton('🛠1 Курс 🧒')
        c2 = KeyboardButton('🚫2 Курс 👦')
        c3 = KeyboardButton('🚫3 Курс 👨')
        c4 = KeyboardButton('🚫4 Курс 👱‍♂')

        return markup.add(c1, c2, c3, c4)

    @staticmethod
    def course1_but():
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ae = KeyboardButton('✅Academic English 1')
        aer = KeyboardButton('✅Academic English Reading')
        c1 = KeyboardButton('✅Calculus 1')
        p1 = KeyboardButton('✅Physics 1')
        pe1 = KeyboardButton('✅Physics Experiment 1')
        intro = KeyboardButton('✅Introduction to IT')
        oop1 = KeyboardButton('✅Object Oriented Programming 1')

        return markup.add(ae, aer, c1, p1, pe1, intro, oop1)

    @staticmethod
    def start():
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn = KeyboardButton('Начать✍')

        return markup.add(btn)

    @staticmethod
    def show():
        btn = ReplyKeyboardMarkup(resize_keyboard=True)
        total = KeyboardButton(text='😳Показать')

        return btn.add(total)