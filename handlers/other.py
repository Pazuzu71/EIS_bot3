from create_bot import dp, bot
from aiogram import F, types, Dispatcher


# @dp.message(F.text)
async def echo(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text=msg.text)


def register_handlers_other(dp: Dispatcher):
    dp.message.register(echo)
