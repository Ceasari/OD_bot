import logging
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import API_TOKEN

API_TOKEN = API_TOKEN

logging.basicConfig(level=logging.INFO)

# create an instance of the bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
