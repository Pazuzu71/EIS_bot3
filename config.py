from dataclasses import dataclass
from environs import Env


default_settings = {}


@dataclass
class FTP_config:
    host: str
    port: int
    login: str
    password: str


@dataclass
class BOT_config:
    token: str
    admin: int


@dataclass
class conf:
    ftp_conf: FTP_config
    bot_conf: BOT_config


def load_config(path: str | None):

    env = Env()  # Создаем экземпляр класса Env
    env.read_env(path)  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

    return conf(
        ftp_conf=FTP_config(
            host=env('HOST'),
            port=env('PORT'),
            login=env('LOGIN'),
            password=env('PASSWORD')
        ),
        bot_conf=BOT_config(
            token=env('TOKEN'),
            admin=env('ADMIN')
        )
    )
