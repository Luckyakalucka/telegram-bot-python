from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from data.config import env
from keyboards.default import menu_day_5, menu_back, menu_class
from loader import dp


@dp.message_handler(Text(equals=["5"]))
async def show_menu(message: Message):
    await message.answer(f"Выбран {message.text} класс. Выберите День недели", reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["🟤 Понедельник 🟤"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 5 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["🟤 Вторник 🟤"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 5 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n",
                             reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["🟤 Среда 🟤"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среда для 5 класса:"
                             f"Дата: {date3}"
                             f"1. {we1}"
                             f"2. {we2}"
                             f"1. {we3}"
                             f"1. {we4}"
                             f"1. {we5}"
                             f"1. {we6}"
                             f"1. {we7}",
                             reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["🟤 Четверг 🟤"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 5 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["🟤 Пятница 🟤"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятница для 5 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_5)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)


env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Природознавство"
mo2 = "Англійська мова"
mo3 = "Українська мова (І) | Інформатика  (ІІ)"
mo4 = "Математика"
mo5 = "Фізкультура"
mo6 = "Основи здоров'я"
mo7 = ""

date2 = env.str("dateTu")
tu1 = "Література"
tu2 = "Математика"
tu3 = "Фізкультура"
tu4 = "Інформатика  (І) | Українська мова (ІІ)"
tu5 = "Німецька мова"
tu6 = "Російська мова"
tu7 = ""

date3 = env.str("dateWe")
we1 = "Математика"
we2 = "Українська мова"
we3 = "Музичне мистецтво"
we4 = "Українська література"
we5 = "Російська мова"
we6 = "Література"
we7 = "ОТМ"

date4 = env.str("dateTh")
th1 = "Англійська мова"
th2 = "Математика"
th3 = "Українська мова"
th4 = "Трудове навчання"
th5 = "Трудове навчання"
th6 = "Українська мова | -"
th7 = ""

date5 = env.str("dateFr")
fr1 = "Природознавство"
fr2 = "Німецька мова"
fr3 = "Англійська мова"
fr4 = "Історія"
fr5 = "Українська література"
fr6 = "Фізкультура"
fr7 = ""
