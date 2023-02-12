from aiogram import Bot, Dispatcher
# from aiogram.dispatcher import dispatcher
from config import TOKEN


bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()
