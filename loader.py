from configparser import ConfigParser
from middlewares.Dataclasses import BotData, DatabaseData

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

cnf = ConfigParser()
cnf.read("conf.ini")

bot_cnf = cnf["TELEGRAM"]
db_cnf = cnf["DATABASE"]

bot_info = BotData(
        bot_cnf["token"],
        bot_cnf["admin"]
)

db_info = DatabaseData(
        db_cnf["user"],
        db_cnf["password"],
        db_cnf["host"],
        int(db_cnf["port"]),
        db_cnf["db"],
)

bot = Bot(bot_info.token)
dp = Dispatcher(bot, storage = RedisStorage2())

del bot_cnf
del db_cnf
