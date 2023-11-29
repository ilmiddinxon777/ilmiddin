from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

turk_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" ЛАХМАДЖУН"),
            KeyboardButton(text="  Долма")
        ],
        [
            KeyboardButton(text=" Искандер кебаб"),
            KeyboardButton(text=" Борек")
        ],
        [
            KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)