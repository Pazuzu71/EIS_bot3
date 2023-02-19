from aiogram import Bot, Dispatcher
from config import load_config


settings = load_config(None)
TOKEN = settings.bot_conf.token
# ID = settings.bot_conf.admin


bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher()
