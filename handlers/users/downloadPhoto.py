from aiogram import types
from aiogram.types import ContentTypes
from loader import dp

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def download(message: types.Message):
    await message.photo[-1].download()
