from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp, bot


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="document saqlab olindi")

@dp.message_handler(content_types=ContentTypes.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="video saqlab olindi")










@dp.message_handler(text="borek")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Turk milliy taomi  borek buning narxi bir porsi 40.000 ming so'm ")

@dp.message_handler(text="Iskander Kebab")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Turk milliy taomi  Iskander Kebab buning narxi bir porsi 100.000 ming so'm ")

@dp.message_handler(text="dolma")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/6?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Turk milliy taomi  dolma buning narxi bir porsi 70.000 ming so'm ")

@dp.message_handler(text="Laxmadjun")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/5?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Turk milliy taomi  Laxmadjun buning narxi bir porsi 55.000 ming so'm ")


""""""""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="Grecheskiy salat")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Evropa milliy taomi  Grecheskiy salat buning narxi bir porsi 30.000 ming so'm ")

@dp.message_handler(text="Xalimu")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Evropa milliy taomi  Xalimu buning narxi bir porsi 130.000 ming so'm ")

@dp.message_handler(text="Paelya")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Evropa milliy taomi  Paelya buning narxi bir porsi 140.000 ming so'm ")

@dp.message_handler(text="Pasta karbonara")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Evropa milliy taomi  Pasta karbonara buning narxi bir porsi 60.000 ming so'm ")


""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="TORT SNICKERS")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  dessert uchun shirinligimiz  TORT SNICKERS buning narxi bir porsi 28.000 ming so'm ")

@dp.message_handler(text="NAPALION TORT")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  dessert uchun shirinligimiz  NAPALION TORT buning narxi bir porsi 22.000 ming so'm ")


@dp.message_handler(text="MEDOVOY TORT")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  dessert uchun shirinligimiz  MEDOVOY TORT buning narxi bir porsi 25.000 ming so'm ")


@dp.message_handler(text="QAYMOQLI TORT")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  dessert uchun shirinligimiz  QAYMOQLI TORT buning narxi bir porsi 28.000 ming so'm ")

""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="Osh")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/20?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu O'zek milliy taomi Osh buning narxi bir porsi 20.000 ming so'm ")


@dp.message_handler(text="Kabob")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/21?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu O'zek milliy taomi Kabob buning narxi bir porsi 25.000 ming so'm ")



@dp.message_handler(text="Sho'rva")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/19?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu O'zek milliy taomi Sho'rva buning narxi bir porsi 15.000 ming so'm ")



@dp.message_handler(text="Somsa")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/16?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu O'zek milliy taomi Somsa buning narxi bir porsi 8.000 ming so'm ")


""""""""""""""""""""""""""""""

@dp.message_handler(text="COCA-COLA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/13?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu COCA-COLA 1l  ichimligi bunin narxi 10.000 ming so'm ")

@dp.message_handler(text="PEPSI 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/10?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  PEPSI 1l  ichimligi bunin narxi 10.000 ming so'm")


@dp.message_handler(text="ARK TEA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/12?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  ARK TEA 1l ichimligi bunin narxi 8.000 ming so'm ")



@dp.message_handler(text="DENA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/11?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu  DENA 1l ichimligi bunin narxi 12.000 ming so'm")

""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="Борек")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Тюретское блюда Борек  один порс этого блюда стоит 40.000 тыс сум")

@dp.message_handler(text="Искандер кебаб")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Тюретское блюда Искандер кебаб  один порс этого блюда стоит 100.000 тыс сум")

@dp.message_handler(text="Долма")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/6?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Тюретское блюда Долма  один порс этого блюда стоит 70.000тыс сум")

@dp.message_handler(text="ЛАХМАДЖУН")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Тюретское блюда ЛАХМАДЖУН  один порс этого блюда стоит 55,000 тыс сум")

""""""""""""""""""""""""""""""

@dp.message_handler(text="TOРT СНИКЕРС")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" Это десерт  TOРT СНИКЕРС один порс этого торта стоит 28.000 тыс сум")

@dp.message_handler(text="TOРT НАПАЛИОН")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это десерт  TOРT НАПАЛИОН один порс этого торта стоит 22.000 тыс сум ")


@dp.message_handler(text="MEДОВОЙ TOРT")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это десерт MEДОВОЙ TOРT один порс этого торта стоит 25.000 тыс сум")


@dp.message_handler(text="СЛИВОЧНЫЙ TOРT")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="BЭто десерт  СЛИВОЧНЫЙ TOРT  один порс этого торта стоит 28.000 тыс сум ")


""""""""""""""""""""""""""

@dp.message_handler(text="DENA 1л")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это напиток DENA 1л его цена 12.000 тыс сум ")

@dp.message_handler(text="ARK TEA 1л")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это напиток ARK TEA 1л его цена 8.000 тыс сум ")

@dp.message_handler(text="PEPSI 1л")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это напиток  PEPSI 1л его цена 10.000 тыс сум ")

@dp.message_handler(text="COCA-COLA 1л")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это напиток COCA-COLA 1л его цена 10.000 тыс сум ")

""""""""""""""""""""""""""""""

@dp.message_handler(text="Плов")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/20"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" Это Узбекское национальное блюда Плов одна порция этого блюда стоит 20,000 тыс сум ")


@dp.message_handler(text="Шашлык")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/21?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" Это Узбекское национальное шашлык блюда одна порция этого блюда стоит 25,000 тыс сум ")



@dp.message_handler(text="Суп")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/19?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" Это Узбекское национальное шашлык блюда одна порция этого блюда стоит   15.000 тыс сум ")



@dp.message_handler(text="Самсы")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/16?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это Узбекское национальное самса блюда одна порция этого блюда стоит   10.000 тыс сум ")

""""""""""""""""""""""""""

@dp.message_handler(text="Греческий салат")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Европейская блюда Греческий салат одно порция этого салата стоит 30,000 тыс сум")

@dp.message_handler(text="Xaлиму")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Европейская блюда Xaлиму одно порция этого салата стоит 130,000 тыс сум ")

@dp.message_handler(text="Пaэлья")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Европейская блюда Пaэлья одно порция этого салата стоит 140,000 тыс сум")

@dp.message_handler(text="Паста Карбонара")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Это национальное Европейская блюда Пaэлья одно порция этого салата стоит 60,000 тыс сум ")

""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="PILOV")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/20?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  national meals Ubekistan PILOV one pors this meal costs 20.000 uzb sum")


@dp.message_handler(text="KEBAB")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/21?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  national meals Ubekistan KEBAB one pors this meal costs 25.000 uzb sum ")



@dp.message_handler(text="SOUP")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/19?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  national meals Ubekistan SOUP one pors this meal costs 15.000 uzb sum  ")



@dp.message_handler(text="SAMSA")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/16?single"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  national meals Ubekistan SAMSA one pors this meal costs 8.000 uzb sum")

""""""""""""""""""""""""""

@dp.message_handler(text="CAKES SNICKERS")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  cake SNICKERS  one pors this meal costs 28.000 uzb sum")

@dp.message_handler(text="NAPALION CAKES")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  NAPALION CAKESS  one pors this meal costs 22.000 uzb sum ")


@dp.message_handler(text="MEDOVOY CAKES")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/22"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's  MEDOVOY CAKES  one pors this meal costs 25.000 uzb sum")


@dp.message_handler(text="CREAMY CAKES")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" It's  CREAMY CAKES  one pors this meal costs 28.000 uzb sum")

""""""""""""""""""""""""""""""""""""

@dp.message_handler(text="DENA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's dirnk DENA 1l costs 12.000 uzb sum ")

@dp.message_handler(text="ARK TEA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's dirnk ARK TEA 1l costs 8.000 uzb sum")

@dp.message_handler(text="PEPSI 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's dirnk PEPSI 1l costs 10.000 uzb sum")

@dp.message_handler(text="COCA-COLA 1l")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's dirnk COCA-COLA 1l costs 10.000 uzb sum ")

""""""""""""""""""""""""""""""""""""""


@dp.message_handler(text="Grecks salat")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/18"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" It's national Europ meal's Grecks salat it's costs 30,000 uzb sum")

@dp.message_handler(text="XALIMU")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption=" It's national Europ meal's Xalimu it's costs 130,000 uzb sum")
@dp.message_handler(text="PAELYA")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Europ meal's Paelya it's costs 140,000 uzb sum")

@dp.message_handler(text="PASTA karbonara")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Europ meal's Pasta karbonara it's costs 60,000 uzb sum")

""""""""""""""""""""""""""""""""


@dp.message_handler(text="borek meals")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Turkish meal's dolma it's costs 40,000 uzb sum")

@dp.message_handler(text="Iskander Kebabs")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Turkish meal's iskander kebab it's costs 100,000 uzb sum")

@dp.message_handler(text="dolma meals")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Turkish meal's dolma it's costs 70,000 uzb sum")

@dp.message_handler(text="Laxmadjun meals")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/ehrasg/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="It's national Turkish  meal's laxmadjun it's costs 55,000 uzb sum")






























