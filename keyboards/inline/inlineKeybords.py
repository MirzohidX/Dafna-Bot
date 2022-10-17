from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


inlinemenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English (Speaking Grammar) ✅", callback_data="curs")
        ],

        [
            InlineKeyboardButton(text="IELTS (Speed UP) ✅", callback_data="ielts")
        ],

        [
            InlineKeyboardButton(text="Prezident Maktabiga Tayyorlov ✅", callback_data="tayyorlov")
        ],

        [
            InlineKeyboardButton(text="Ona Tili ✅", callback_data="ona")
        ],

        [
            InlineKeyboardButton(text="Matematika✅", callback_data="matematika")
        ],

        [
            InlineKeyboardButton(text="Mental Arifmetika ✅", callback_data="mental")
        ],

        [
            InlineKeyboardButton(text="Kimyo ✅", callback_data="kimyo")
        ],

        [
            InlineKeyboardButton(text="Koreys tili ✅", callback_data="koreys")
        ],

        [
            InlineKeyboardButton(text="Yapon tili ✅", callback_data="yapon")
        ],

        # [
        #     InlineKeyboardButton(text="Orqaga ↩️", callback_data=)
        # ],

        # [
        #     InlineKeyboardButton(text="Admin", url='https://t.me/Zohidjaan')
        # ],
    ],
)