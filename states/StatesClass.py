"""
Класс для хранения состояний бота
"""

from aiogram.dispatcher.filters.state import StatesGroup, State

class BotStates(StatesGroup):
    main = State()
    about_numerology = State()
    gift = State()