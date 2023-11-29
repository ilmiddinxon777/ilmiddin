from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  Osh"),
            KeyboardButton(text="  Kabob")
        ],
        [
            KeyboardButton(text="  Sho'rva"),
            KeyboardButton(text="  Somsa")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)


tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)
