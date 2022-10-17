from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from keyboards.default.StartKeyborad import menu
from utils.db_api.postgres import send_ex

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    try:
        user = send_ex(f"""INSERT INTO baza2 (name, username, user_id) 
                        VALUES ('{message.from_user.full_name}','@{message.from_user.username}',{message.from_user.id}) 
                        returning *""")
        await message.answer(f"Assalomu alaykum {message.from_user.full_name} <b>Dafna Education</b> botga xush kelibsiz!\n\n"
                             f"<b>Tanishish</b> tugmasini bosing va biz bilan olg'a qadam bosing", reply_markup=menu)



    except:
        await message.reply(f"Assalomu alaykum {message.from_user.full_name} bizning bazamizda borsiz!\n\n"
                            f"<b>Tanishish</b> tugmasini bosing va biz bilan olg'a qadam bosing", reply_markup=menu)

@dp.message_handler(IsPrivate(), commands='jadval')
async def jadval(message: types.Message):
    jadval1 = send_ex(f"""SELECT *FROM english """)
    await message.answer(f"Sizning Jadvalingiz natijasi:\n{jadval1}")