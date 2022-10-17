from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup

from loader import dp

@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.get_mention(as_html=True)} siz guruhdasiz !")

@dp.message_handler(IsGroup(), commands='bot')
async def bot(message: types.Message):
    await  message.answer('Botdan foydalanish uchun @Dafna_Education_bot')
