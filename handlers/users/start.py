from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate

from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name} wikipedia botga xush kelibsiz!")
    await message.answer(f"O'zingizga kerakli ma'lumotni izlab toping")