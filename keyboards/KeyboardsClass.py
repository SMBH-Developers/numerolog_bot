"""
Класс для хранения всех клавиатур бота
"""

from aiogram import types


class AllKeyboards:
    ...


class GenerateKeyboard:
    def __init__(self, text: str | list[str], rows: int = 1):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=rows)
        if isinstance(text, list):
            for txt in text:
                kb.row(txt)
            self.kb = kb
            return

        kb.row(text)
        self.kb = kb


mrkup_2h = types.InlineKeyboardMarkup()
mrkup_2h.add(types.InlineKeyboardButton(text='🔑 НАПИСАТЬ АДЕЛЬ 🔑', url='https://t.me/numerolog_mentor'))
mrkup_24h = types.InlineKeyboardMarkup()
mrkup_24h.add(types.InlineKeyboardButton(text='✨ ДИАГНОСТИКА СУДЬБЫ ✨', url='https://t.mnumerolog_mentor'))
mrkup_48h = types.InlineKeyboardMarkup()
mrkup_48h.add(types.InlineKeyboardButton(text='🎁 Бесплатная консультация 🎁', url='https://t.me/numerolog_mentor'))
mrkup_72h = types.InlineKeyboardMarkup()
mrkup_72h.add(types.InlineKeyboardButton(text='✍️ Получить консультацию', url='https://t.me/numerolog_mentor'))
