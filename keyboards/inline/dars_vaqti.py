from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

dars_kuni = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣ Dushanba Chorshanba Juma", callback_data="Dushanba_Chorshanba_Juma")
        ],
        [
            InlineKeyboardButton(text="2️⃣ Seshanba Payshanba Shanba", callback_data="Seshanba_Payshanba_Shanba")
        ]
    ],
)
dars_soatlari = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🕣 08:00 -> 10:00', callback_data="08:00-10:00"),
            InlineKeyboardButton(text="🕙 10:00 -> 12:00", callback_data="10:00-12:00")
        ],
        [
            InlineKeyboardButton(text="🕑 14:00 -> 16:00", callback_data="14:00-16:00"),
            InlineKeyboardButton(text="🕓 16:00 -> 18:00", callback_data="16:00-18:00")
        ],
        [
            InlineKeyboardButton(text="🕕 18:00 -> 20:00", callback_data="18:00-20:00")
        ]
    ]
)


