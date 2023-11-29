from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  БЛЮДЫ "),
            KeyboardButton(text=" НАПИТКИ  "),
        ],
        [
            KeyboardButton(text=" ЕВРОПЕЙСКИЕ БЛЮДЫ ")
        ],
        [
            KeyboardButton(text=" СЛАДОСТИ "),
            KeyboardButton(text=" ТУРЕТСКИЕ БЛЮДЫ "),
        ],
        [
            KeyboardButton(text="Локатция",request_location=True),
            KeyboardButton(text="Контакт",request_contact=True)
        ],
        [
            KeyboardButton(text=" Вибырите другой язык"),
            KeyboardButton(text="Обрашение к админу")
        ]
    ],
    resize_keyboard=True
)


