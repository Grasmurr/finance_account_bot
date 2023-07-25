from loader import bot, dp
from aiogram import executor
from handlers import dp, bot


def start_polling():
    executor.start_polling(dp, skip_updates=True, on_startup=message_on_startup, on_shutdown=message_on_shutdown)


async def message_on_startup(dp):
    await bot.send_message(chat_id=305378717, text='Bot active!')


async def message_on_shutdown(dp):
    await bot.send_message(chat_id=305378717, text='Bot off!')

if __name__ == '__main__':
    start_polling()

