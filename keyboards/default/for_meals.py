from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" PILOV"),
            KeyboardButton(text="  KEBAB")
        ],
        [
            KeyboardButton(text="  SOUP"),
            KeyboardButton(text=" SAMSA")
        ],
        [
            KeyboardButton(text='Backwarda')
        ]
    ],
    resize_keyboard=True
)