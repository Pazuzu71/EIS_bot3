from create_bot import dp, bot
from handlers import client, admin, other


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


dp.run_polling(bot)
