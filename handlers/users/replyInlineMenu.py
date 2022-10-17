from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.inlinekey import course_info

# @dp.callback_query_handler(text="curs")
# async def english(call : CallbackQuery):
#
#     await call.message.answer("<b>English (Speaking Grammar)</b> kursi tanlandi.\nMarhamat kurs bilan tanishing 👇\n\n🗓Davomiyligi:  10 oy - 11 oy\n📕Samaradorligi:  7.5 +\n🎓O'qituvchi:  Shahzod Qayumov IELTS 7.5\n🕐Vaqti:  O'ziz bo'sh vaqtiga qo'yasiz\n💳To'lov:  Naxt & Plastik\n💰Narxi: 250 000 - 300 000 ming.", reply_markup=hardverekey)
#     await call.message.delete()

# @dp.callback_query_handler(text="ielts")
# async def ielts(call : CallbackQuery):
#     await call.message.answer("<b>IELTS (Speed UP)</b> kursi tanlandi.\nMarhamat kurs bilan tanishing 👇\n\n🗓Davomiyligi:  6 oy - 8 oy\n📕Samaradorligi:  8 +\n🎓O'qituvchi: Shahzod Qayumov IELTS 7.5\n🕐Vaqti:  O'ziz bo'sh vaqtiga qo'yasiz\n💳To'lov:  Naxt & Plastik\n💰Narxi: 250 000 - 300 000 ming.", reply_markup=course_info)
#     await call.message.delete()

@dp.callback_query_handler(text="python")
async def books(call : CallbackQuery):
    await call.message.answer("Python kursi tanlandi")