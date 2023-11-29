from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  TAOMLAR"),
            KeyboardButton(text="  ICHIMLIKAR"),
        ],
        [
            KeyboardButton(text=" EVROPA MILLIY TAOMLARI")
        ],
        [
            KeyboardButton(text="  shrinliklar"),
            KeyboardButton(text="  TURK TAOMLARI"),
        ],
        [
            KeyboardButton(text="lokatsiya",request_location=True),
            KeyboardButton(text="kontakt",request_contact=True)
        ],
        [
            KeyboardButton(text="Boshqa tilni tanlash"),
            KeyboardButton(text="Adminga murojat")
        ]
    ],
    resize_keyboard=True
)