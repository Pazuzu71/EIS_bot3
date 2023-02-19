from create_bot import dp, bot
from keyboards import set_menu
from handlers import client, admin, other
from DB.db_utils import database_create


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    dp.startup.register(set_menu.set_main_menu)
    db = database_create()
    db.disconnect()
    dp.run_polling(bot)
