import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters.admins import AdminFilter
from filters.group_filters import IsGroup
from loader import dp, bot


# /ro oki !ro (read-only) komandalari uchun handler
@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    print(parsed)
    time = parsed.group(2)
    comment = parsed.group(3)
    # print(time)
    if not time:
        time = 10

    time = int(time)
    print(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)
    print(until_date)
    # try:
    await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
    await message.reply_to_message.delete()
    # except aiogram.utils.exceptions.BadRequest as err:
    #     await message.answer(f"Xato! {err.args}")
    #     return

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
                         f"Sabab: \n<b>{comment}</b>")

    service_message = await message.reply("Xabar 10 sekunddan so'ng o'chadi.")
    await asyncio.sleep(10)
    await message.delete()
    await service_message.delete()

@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("Xabar 10 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(10)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi <b>{member.full_name}</b> tiklandi")
    await message.delete()
    await service_message.delete()

# Foydalanuvchini gruxdan quvlash
@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    asd = await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(10)
    await message.delete()
    await service_message.delete()
    await asd.delete()
    await message.reply_to_message.delete()

# Foydalanuvchiga gr ga qo'shilish imkonini berish (o'zi qo'shilishi mumkin)
@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} grga qo'shilish mumkin")
    service_message = await message.reply("Xabar 10 sekunddan so'ng o'chadi")

    await asyncio.sleep(10)

    await message.delete()
    await service_message.delete()