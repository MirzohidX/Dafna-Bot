from aiogram import types
from loader import dp
from keyboards.inline.inlineKeybords import inlinemenu

@dp.message_handler(text="Tanishish🚀")
async def products(message: types.Message):
    await message.answer("Marxamat kurslar bilan tanishing 👇",reply_markup=inlinemenu)

# @dp.message_handler(text="Courses")
# async def pchandler(call: types.ContentTypes):
#     print(call)