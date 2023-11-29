from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

turk_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  Laxmadjun"),
            KeyboardButton(text="dolma")
        ],
        [
            KeyboardButton(text="  Iskander Kebab"),
            KeyboardButton(text="  borek")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)