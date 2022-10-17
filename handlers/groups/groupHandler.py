import datetime
import re
# import Command
import aiogram.utils.exceptions
from aiogram import types
from loader import dp, bot
from filters.group_filters import IsGroup

import io


@dp.message_handler(IsGroup(), commands='start')
async def noder(message: types.Message):
    await message.answer('Salom Guruhga xush kelibsiz')


@dp.message_handler(IsGroup(), commands='change')
async def qwerty(message: types.Message):
    text = message.reply_to_message.text
    print(text)
    await bot.set_chat_title(message.chat.id, title=text)


@dp.message_handler(IsGroup(), commands='ch_photo')
async def qwerty(message: types.Message):
    photo = message.reply_to_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    print(photo)
    await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)


