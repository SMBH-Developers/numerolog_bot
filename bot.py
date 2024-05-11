import asyncio

from loguru import logger
from aiogram.utils import markdown
from aiogram import exceptions, executor

from keyboards import *
from loader import dp, bot
from Database import DataBase
from handlers.user import main_handler

db = DataBase()


async def sending_messages_2h():
    while True:
        try:
            await asyncio.sleep(7)

            text = f'🩷 Спешу напомнить остается всего 6 мест на {markdown.hbold("бесплатный нумерологический разбор")} от эксперта Адель. Просто напишите ей в личку 👉 @numerolog_mentor слово {markdown.hbold("Разбор")} и узнайте, какие послания содержит ваша дата рождения.'

            users = db.get_users_2h_autosending()
            for user in users:
                try:
                    await bot.send_message(user, text=text, parse_mode='html', reply_markup=mrkup_2h)
                    logger.info(f'ID: {user}. Получил рассылку 2 Часа')
                    db.mark_got_2h_autosending(user)
                    await asyncio.sleep(0.2)
                except (exceptions.BotBlocked, exceptions.ChatNotFound, exceptions.UserDeactivated):
                    logger.error(f'ID: {user}. DELETED')
                    db.delete_user(user)
                except Exception as ex:
                    logger.error(f'got error: {ex}')
        except Exception as ex:
            await bot.send_message(1371617744, f'Happened: {ex}')


async def sending_messages_24h():
    while True:
        try:
            await asyncio.sleep(7)

            text = f'😎 90% людей обращаются к различным эскпертам, {markdown.hbold("чтобы узнать свое предназначение")} и методы улучшения качества жизни. Сегодня эксперт Адель предлагает бесплатную консультацию {markdown.hbold("Диагностика судьбы")} для  5 желающих. Записать Вас?'

            users = db.get_users_24h_autosending()
            for user in users:
                try:
                    await bot.send_message(user, text=text, parse_mode='html', reply_markup=mrkup_24h)
                    logger.info(f'ID: {user}. Получил рассылку 24 Часа')
                    db.mark_got_24h_autosending(user)
                    await asyncio.sleep(0.2)
                except (exceptions.BotBlocked, exceptions.ChatNotFound, exceptions.UserDeactivated):
                    logger.error(f'ID: {user}. DELETED')
                    db.delete_user(user)
                except Exception as ex:
                    logger.error(f'got error: {ex}')
        except Exception as ex:
            await bot.send_message(1371617744, f'Happened: {ex}')


async def sending_messages_48h():
    while True:
        try:
            await asyncio.sleep(7)

            text = f'{markdown.hbold("Сегодня мощные энергетические лунные сутки.")}\n\n 🤩 Это сильный день, когда через подсознание можно скорректировать сценарий жизни. В такие дни наш нумеролог Адель для своих подписчиков дает бесплатные консультации.\n\n Успеет принять {markdown.hbold("10 человек")}, которые первыми напишут ей в личные сообщения @numerolog_mentor👈 .'

            users = db.get_users_48h_autosending()
            for user in users:
                try:
                    await bot.send_message(user, text=text, parse_mode='html', reply_markup=mrkup_48h)
                    logger.info(f'ID: {user}. Получил рассылку 24 Часа')
                    db.mark_got_48h_autosending(user)
                    await asyncio.sleep(0.2)
                except (exceptions.BotBlocked, exceptions.ChatNotFound, exceptions.UserDeactivated):
                    logger.error(f'ID: {user}. DELETED')
                    db.delete_user(user)
                except Exception as ex:
                    logger.error(f'got error: {ex}')
        except Exception as ex:
            await bot.send_message(1371617744, f'Happened: {ex}')


async def sending_messages_72h():
    while True:
        try:
            await asyncio.sleep(7)

            text = f'А вы знали, что по дате рождения можно узнать, что {markdown.hbold("ограничивает")} ваш финансовый потенциал🫰🏾, что мешает встретить свою любовь♥️ или сгармонизировать текущие отношения с партнером.👩‍❤️‍👨\n {markdown.hbold("Последние дни в этом месяце")} когда можно получить бесплатную консультацию от нумеролога @numerolog_mentor'

            users = db.get_users_72h_autosending()
            for user in users:
                try:
                    await bot.send_message(user, text=text, parse_mode='html', reply_markup=mrkup_72h)
                    logger.info(f'ID: {user}. Получил рассылку 24 Часа')
                    db.mark_got_72h_autosending(user)
                    await asyncio.sleep(0.2)
                except (exceptions.BotBlocked, exceptions.ChatNotFound, exceptions.UserDeactivated):
                    logger.error(f'ID: {user}. DELETED')
                    db.delete_user(user)
                except Exception as ex:
                    logger.error(f'got error: {ex}')
        except Exception as ex:
            await bot.send_message(1371617744, f'Happened: {ex}')


async def on_startup(_):
    asyncio.create_task(sending_messages_2h())
    asyncio.create_task(sending_messages_24h())
    asyncio.create_task(sending_messages_48h())
    asyncio.create_task(sending_messages_72h())


#async def bot_start_pooling():
#    try:
#        await executor.start_polling(dp, on_startup=on_startup)
#    finally:
#        logger.info("Bot was closed")
        # await dp.storage.close()


if __name__ == "__main__":
    #asyncio.run(bot_start_pooling())
    executor.start_polling(dp, on_startup=on_startup)
