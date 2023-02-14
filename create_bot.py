from aiogram import Bot, Dispatcher
from environs import Env


env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

TOKEN = env('TOKEN')  # Сохраняем значение переменной окружения в переменную TOKEN
ID = env.int('ID')  # Преобразуем значение переменной окружения к типу int
# и сохраняем в переменной ID

# print(TOKEN)
# print(ID)
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()
