from aiogram.types import CallbackQuery, Message
from loader import dp, bot
from keyboards.inline.inlinekey import course_info,yes_no
from states.course_state import EnglishState
from aiogram.dispatcher import FSMContext
from utils.db_api.postgres import send_ex
from keyboards.inline.inlineKeybords import inlinemenu
from keyboards.inline.dars_vaqti import dars_kuni, dars_soatlari

import re
r_phone = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

@dp.callback_query_handler(text="tayyorlov")
async def english(call : CallbackQuery):

    await call.message.answer("<b>Prezident Maktabiga Tayyorlov</b> kursi tanlandi.\n"
                              "Marhamat kurs bilan tanishing 👇\n\n🗓Davomiyligi:   Haftasiga 3 marta\n"
                              "📕Samaradorligi:  Prezident maktabiga kirish imkoniyati\n🎓O'qituvchi:  Janobiddin Fazliddinov\n"
                              "🛠Tajriba: 3 yil\n"
                              "🕐Vaqti:  O'ziz bo'sh vaqtiga qo'yasiz\n"
                              "💳To'lov:  Naxt & Plastik\n💰Narxi: 150.000 so'm/Har oy", reply_markup=course_info)
    await call.message.delete()

@dp.callback_query_handler(text="orqaga")
async def orqaga(call : CallbackQuery):
    await call.message.answer('Marxamat kurslar bilan tanishing 👇',reply_markup=inlinemenu)
    await call.message.delete()

@dp.callback_query_handler(text="ky")
async def rigester(call: CallbackQuery):
    await EnglishState.button.set()
    await call.message.answer("Yaxshi, endi sizdan so'raladigan ma'lumotlarni bexato kriting")
    await call.message.answer("Endi Ism Familiyangizni yozib qoldiring?")
    await call.message.delete()
    await EnglishState.next()


@dp.message_handler(state=EnglishState.full_name)
async def entr_full_name(message: Message, state=FSMContext):
    full_name = message.text
    await state.update_data(
        {"full_name":full_name}
    )
    await message.answer("Endi telefon raqamingizni xatosiz yuboring")
    await EnglishState.next()


@dp.message_handler(state=EnglishState.phone)
async def entr_phone(message: Message, state=FSMContext):
    phone = message.text
    if re.search(r_phone, phone):

        await state.update_data(
            {"phone": phone}
        )
        await message.answer("O'zingizga maqul kunni tanlang", reply_markup=dars_kuni)
        await EnglishState.next()
    else:
        await message.answer("Kchirasiz telfon raqamingizni to'g'ri kriting")


@dp.callback_query_handler(state=EnglishState.days)
async def days(call: CallbackQuery, state=FSMContext):
    date = call.data
    await state.update_data(
        {"date":date}
    )
    await call.message.answer("O'zingizga qulay vaqtni tanlang", reply_markup=dars_soatlari)
    await call.message.delete()
    await EnglishState.next()


@dp.callback_query_handler(state=EnglishState.time)
async def times(call: CallbackQuery, state = FSMContext):
    time = call.data
    await state.update_data(
        {"time":time}
    )
    await call.message.delete()


    data = await state.get_data()
    # user = Message.from_user.first_name
    f_name = data.get("full_name")
    phone = data.get("phone")
    k_date = data.get("date")
    k_time = data.get("time")
    # k_userid = data.get("user_id")

    # first_name.get_mention(as_html=True)

    await bot.send_message(chat_id=1871081893, text=f"O'quvchi: \n"
                                                    f"Ismi: {f_name}\n"
                                                    f"Telefon raqami: {phone}\n"
                                                    f"Kunlari: {k_date}\n"
                                                    f"Vaqti: {k_time}\n"
                                                    f"Kursi:  English (Speaking Grammar)")

    await call.message.answer("Malumotlaringiz qabul qilindi adminlarimiz sizga aloqaga chiqishadi")

    send_ex(f"""INSERT INTO english (full_name, phone, date, time)
                                VALUES ('{f_name}','{phone}','{k_date}','{k_time}')
                                returning *""")
    await state.finish()


@dp.callback_query_handler(text="kh", state=EnglishState.button)
async def backend(call: CallbackQuery, state = FSMContext):
    info = send_ex("select english from subjects_info")
    await call.message.answer(info[0][0])
    await call.message.answer("Kursga ro'yxatdan o'tishni xoxlaysizmi",reply_markup=yes_no)

@dp.callback_query_handler(text="yes", state=EnglishState.button)
async def choes(call: CallbackQuery, state = FSMContext):
    await call.message.answer("marxamat",reply_markup=course_info)
    await call.message.delete()

@dp.callback_query_handler(text="no", state=EnglishState.button)
async def choes(call: CallbackQuery, state = FSMContext):
    await call.message.answer("Boshqa kurslarga tashrif buyurishingiz mumkin", reply_markup=inlinemenu)
    await call.message.delete()
    await state.finish()




