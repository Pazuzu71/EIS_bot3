from create_bot import dp, bot
from aiogram import types, F, Dispatcher
from aiogram.filters import Command
from config import default_settings


'''На старте проверяем есть ли пользователь в настройках по умолчанию. 
Если нет, прогоняем через машину состояний и заполняем таблицу по пользователю'''
# TODO машины состояний пока нет, надо сделать
async def start(msg: types.Message):
    if msg.from_user.id in default_settings.keys():
        pass
        # TODO надо где-то хранить настройки по умолчанию, временно в словаре в конфиге, переделать на базу
    else:
        await msg.delete()
        await bot.send_message(msg.from_user.id, 'Настройки по умолчанию')


def register_handlers_client(dp: Dispatcher):
    dp.message.register(start, Command(commands=['start'], ignore_case=True))
