from aiogram.dispatcher.filters.state import State, StatesGroup


class AeStates(StatesGroup):
    main = State()
    attendance = State()
    discussion = State()
    quiz = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()


class AerStates(StatesGroup):
    main = State()
    attendance = State()
    quiz = State()
    midScore = State()
    finScore = State()
    total = State()


class ITStates(StatesGroup):
    main = State()
    attendance = State()
    assignments = State()
    quiz = State()
    midScore = State()
    finScore = State()
    total = State()


class OOP1States(StatesGroup):
    main = State()
    attendance = State()
    quiz = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()


class P1States(StatesGroup):
    main = State()
    hw_ass_att = State()
    midScore = State()
    finScore = State()
    total = State()


class PeStates(StatesGroup):
    main = State()
    attendance = State()
    lab = State()
    total = State()


class C1States(StatesGroup):
    main = State()
    attendance = State()
    assignments = State()
    midScore = State()
    finScore = State()
    total = State()
