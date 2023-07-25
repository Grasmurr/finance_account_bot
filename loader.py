from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

TOKEN = config('BOT_TOKEN')

bot = Bot(TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
