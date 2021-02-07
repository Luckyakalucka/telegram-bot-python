from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_9, menu_class
from loader import dp


@dp.message_handler(Text(equals=["9"]))
async def show_menu(message: Message):
    await message.answer(f"Выбран {message.text} класс. Выберите День недели", reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["🔵 Понедельник 🔵"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 9 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["🔵 Вторник 🔵"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 9 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n"
                             f"8. {tu8}\n",
                             reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["🔵 Среда 🔵"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среду для 9 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n"
                             f"8. {we8}\n",
                             reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["🔵 Четверг 🔵"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 9 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["🔵 Пятница 🔵"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятницу для 9 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_9)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)

env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Фізика"
mo2 = "Фізика"
mo3 = "Геометрія"
mo4 = "Історія України"
mo5 = "Література"
mo6 = "Українська література"
mo7 = "Фізкультура"

date2 = env.str("dateTu")
tu1 = "Англійська мова"
tu2 = "Німецька мова"
tu3 = "Російська мова"
tu4 = "Всесвітня історія"
tu5 = "Хімія"
tu6 = "Алгебра"
tu7 = "Інформатика (І)"
tu8 = "Інформатика (І)"

date3 = env.str("dateWe")
we1 = "Фізика"
we2 = "Біологія"
we3 = "Основи здоров'я | Історія України"
we4 = "Німецька мова"
we5 = "Геометрія"
we6 = "Українська мова"
we7 = "Література"
we8 = "Фізкультура"

date4 = env.str("dateTh")
th1 = "Фізкультура"
th2 = "Правознавство"
th3 = "Трудове навчання"
th4 = "Географія"
th5 = "Мистецтво"
th6 = "Українська мова"
th7 = "Українська література"

date5 = env.str("dateFr")
fr1 = "Англійська мова"
fr2 = "Біологія"
fr3 = "Алгебра"
fr4 = "Хімія"
fr5 = "Російська мова"
fr6 = "Інформатика (ІІ)"
fr7 = "Інформатика (ІІ)"