from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shirinliklar_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  TOРT СНИКЕРС "),
            KeyboardButton(text="  MEДОВОЙ TOРT ")
        ],
        [
            KeyboardButton(text=" TOРT НАПАЛИОН "),
            KeyboardButton(text=" СЛИВОЧНЫЙ TOРT ")
        ],
        [
            KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)