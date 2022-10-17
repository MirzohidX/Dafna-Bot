from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.inlineKeybords import inlinemenu


course_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursga yozilish ✍️", callback_data="ky")
        ],
        [
            InlineKeyboardButton(text="Orqaga ↩️", callback_data="orqaga")
        ],
    ]
)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha✅", callback_data="yes"),
            InlineKeyboardButton(text="Yo'q❌", callback_data="no")
        ],
    ],
)
