from create_bot import dp, bot
from handlers import client, other


client.register_handlers_client(dp)
other.register_handlers_other(dp)


dp.run_polling(bot)
