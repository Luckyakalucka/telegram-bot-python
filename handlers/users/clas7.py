from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_7, menu_class
from loader import dp


@dp.message_handler(Text(equals=["7"]))
async def show_menu(message: Message):
    await message.answer(f"Выбран {message.text} класс. Выберите День недели", reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["⚪ Понедельник ⚪"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 7 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["⚪ Вторник ⚪"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 7 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n",
                             reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["⚪ Среда ⚪"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среда для 7 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n",
                             reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["⚪ Четверг ⚪"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 7 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["⚪ Пятница ⚪"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятница для 7 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_7)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)

env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Література"
mo2 = "Історія України"
mo3 = "Біологія"
mo4 = "Фізика"
mo5 = "Німецька мова"
mo6 = "Фізкультура"
mo7 = "Російська мова"

date2 = env.str("dateTu")
tu1 = "Основи здоров'я"
tu2 = "Хімія"
tu3 = "Географія"
tu4 = "Українська мова"
tu5 = "Алгебра"
tu6 = "Українська література"
tu7 = "Російська мова"

date3 = env.str("dateWe")
we1 = "ОТМ"
we2 = "Всесвітня історія"
we3 = "Геометрія"
we4 = "Фізика"
we5 = "Англійська мова"
we6 = "Фізкультура"
we7 = "Інформатика (ІІ)"

date4 = env.str("dateTh")
th1 = "Інформатика (І)"
th2 = "Німецька мова"
th3 = "Географія"
th4 = "Алгебра"
th5 = "Українська література"
th6 = "Трудове навчання"
th7 = "Фізкультура"

date5 = env.str("dateFr")
fr1 = "Геометрія"
fr2 = "Англійська мова"
fr3 = "Література"
fr4 = "Музичне мистецтво"
fr5 = "Українська мова"
fr6 = "Хімія | Українська мова"
fr7 = "Біологія"