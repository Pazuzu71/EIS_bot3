from create_bot import dp, bot
from aiogram import types, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from ftp.ftp_download import get_list
from config import load_config


settings = load_config(None)
host = settings.ftp_conf.host
port = settings.ftp_conf.port
login = settings.ftp_conf.login
password = settings.ftp_conf.password


btn: KeyboardButton = KeyboardButton(text='скачать')
kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[btn]], resize_keyboard=True)


async def download_from_ftp_current(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text='Нажми скачать, чтобы закачать целую папку с ФТП', reply_markup=kb)


async def get_from_frp(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text='сейчас скачаю')
    await get_list(host, port, login, password)


def register_handlers_admin(dp: Dispatcher):
    dp.message.register(download_from_ftp_current, Command(commands=['down'], ignore_case=True))
    dp.message.register(get_from_frp, F.text == 'скачать')
