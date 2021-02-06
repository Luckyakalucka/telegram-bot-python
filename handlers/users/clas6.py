from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu_day_6, menu_class
from loader import dp


@dp.message_handler(Text(equals=["6"]))
async def show_menu(message: Message):
    await message.answer(f"Выбрын {message.text} класс. Выберите День недели", reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["⚫ Понедельник ⚫"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 6 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["⚫ Вторник ⚫"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 6 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n",
                             reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["⚫ Среда ⚫"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среда  для 6 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n",
                             reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["⚫ Четверг ⚫"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 6 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["⚫ Пятница ⚫"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятница для 6 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_6)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)


date1 = ""
mo1 = ""
mo2 = ""
mo3 = ""
mo4 = ""
mo5 = ""
mo6 = ""
mo7 = ""

date2 = ""
tu1 = ""
tu2 = ""
tu3 = ""
tu4 = ""
tu5 = ""
tu6 = ""
tu7 = ""

date3 = ""
we1 = ""
we2 = ""
we3 = ""
we4 = ""
we5 = ""
we6 = ""
we7 = ""

date4 = ""
th1 = ""
th2 = ""
th3 = ""
th4 = ""
th5 = ""
th6 = ""
th7 = ""

date5 = ""
fr1 = ""
fr2 = ""
fr3 = ""
fr4 = ""
fr5 = ""
fr6 = ""
fr7 = ""