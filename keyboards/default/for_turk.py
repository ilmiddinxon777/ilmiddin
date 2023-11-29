from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

turk_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  Laxmadjun meals"),
            KeyboardButton(text="  dolma meals")
        ],
        [
            KeyboardButton(text="  Iskander Kebabs"),
            KeyboardButton(text="  borek meals")
        ],
        [
            KeyboardButton(text='Backward')
        ]
    ],
    resize_keyboard=True
)