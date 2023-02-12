from create_bot import dp, bot
from handlers import other


other.register_handlers_other(dp)


dp.run_polling(bot)
