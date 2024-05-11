from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from texts import Texts
from states import BotStates
from keyboards import GenerateKeyboard

from Database import DataBase


db = DataBase()


@dp.message_handler(commands="start", state="*")
async def start_handler(message: types.Message):
    buttons = [
        "📜Узнать про нумерологию больше",
        "🎁Получить бесплатный анализ"
    ]
    if not db.check_if_user_exist(message.from_user.id):
        db.registartion_user(message.from_user.id)

    await message.answer(Texts.start_text, reply_markup=GenerateKeyboard(buttons, 2).kb)
    await BotStates.main.set()


@dp.message_handler(state=BotStates.main)
async def main_handler(message: types.Message, state: FSMContext):
    if message.text == "📜Узнать про нумерологию больше":
        buttons = [
            "🤔Что такое нумерология?",
            "✴️Откуда к нам пришла нумерология?",
            "🔭Что можно узнать с помощью нумерологии",
            "👼Что такое число Ангела?",
            "🪅Что такое число судьбы?",
            "🪐Что такое число года",
            "👈Назад"
        ]
        await message.answer(Texts.more_about_numerology, reply_markup=GenerateKeyboard(buttons, 3).kb)
        await BotStates.about_numerology.set()

    if message.text == "🎁Получить бесплатный анализ":
        await message.answer(Texts.get_free_analize, reply_markup=GenerateKeyboard("👈Назад").kb)
        await BotStates.gift.set()

    return


@dp.message_handler(state=BotStates.gift)
async def gift_handler(message: types.Message, state: FSMContext):
    if message.text == "👈Назад":
        if message.text == "👈Назад":
            buttons = [
            "📜Узнать про нумерологию больше",
            "🎁Получить бесплатный анализ"
            ]
            await message.answer(Texts.start_text, reply_markup=GenerateKeyboard(buttons, 2).kb)
            await BotStates.main.set()


@dp.message_handler(state=BotStates.about_numerology)
async def about_numerology(message: types.Message, state: FSMContext):
    if message.text == "🤔Что такое нумерология?":
        await message.answer(Texts.about_numerology)

    if message.text == "✴️Откуда к нам пришла нумерология?":
        await message.answer(Texts.where_numerology)

    if message.text == "🔭Что можно узнать с помощью нумерологии":
        await message.answer(Texts.what_can_you_find_out)

    if message.text == "👼Что такое число Ангела?":
        await message.answer(Texts.what_is_angel_numeric)

    if message.text == "🪅Что такое число судьбы?":
        await message.answer(Texts.what_is_fate_numeric)

    if message.text == "🪐Что такое число года":
        await message.answer(Texts.what_is_year_numeric)

    if message.text == "👈Назад":
        buttons = [
        "📜Узнать про нумерологию больше",
        "🎁Получить бесплатный анализ"
        ]
        await message.answer(Texts.start_text, reply_markup=GenerateKeyboard(buttons, 2).kb)
        await BotStates.main.set()

    return