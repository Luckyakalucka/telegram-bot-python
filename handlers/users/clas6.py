from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_6, menu_class
from loader import dp


@dp.message_handler(Text(equals=["6"]))
async def show_menu(message: Message):
    await message.answer(f"Выбран {message.text} класс. Выберите День недели", reply_markup=menu_day_6)

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


env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Фізкультура"
mo2 = "Біологія"
mo3 = "Російська мова"
mo4 = "Англійська мова"
mo5 = "Українська мова"
mo6 = "Українська література"
mo7 = "Інформатика (І)"

date2 = env.str("dateTu")
tu1 = "Математика"
tu2 = "Українська мова"
tu3 = "Література"
tu4 = " Німецька мова"
tu5 = "Російська мова"
tu6 = "Основи здоров'я"
tu7 = "ОТМ"

date3 = env.str("dateWe")
we1 = "Біологія"
we2 = "Математика"
we3 = "Англійська мова"
we4 = "Географія"
we5 = "Історія"
we6 = "Інформатика (ІІ)"
we7 = ""

date4 = env.str("dateTh")
th1 = "Українська мова"
th2 = "Українська література"
th3 = "Математика"
th4 = "Трудове навчання"
th5 = "Трудове навчання"
th6 = "Фізкультура"
th7 = "- | Українська мова"

date5 = env.str("dateFr")
fr1 = "Історія"
fr2 = "Математика"
fr3 = "Музичне мистецтво"
fr4 = "Німецька мова"
fr5 = "Географія"
fr6 = "Література"
fr7 = "Фізкультура"