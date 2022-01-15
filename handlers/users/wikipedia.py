from aiogram import types

from loader import dp


import logging
logging.basicConfig(level=logging.INFO)
import wikipedia

wikipedia.set_lang('uz')
@dp.message_handler()
async def wikesend (message: "type.message"):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer(f"Kechirasiz {message.from_user.full_name} bu mavzuga oid wikipedia topilmadi" )


