from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_10, menu_class
from loader import dp


@dp.message_handler(Text(equals=["10"]))
async def show_menu(message: Message):
    await message.answer(f"Выбрын {message.text} класс. Выберите День недели", reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["🔴 Понедельник 🔴"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 10 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["🔴 Вторник 🔴"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 10 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n"
                             f"8. {tu8}\n",
                             reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["🔴 Среда 🔴"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среду для 10 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n",
                             reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["🔴 Четверг 🔴"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 10 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["🔴 Пятница 🔴"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятницу для 10 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_10)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)

env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Історія України"
mo2 = "Зарубіжна література"
mo3 = "Історія України"
mo4 = "Захист України"
mo5 = "Інформатика (д) | Захист України (хл)"
mo6 = "Геометрія"
mo7 = "Фізкультура"

date2 = env.str("dateTu")
tu1 = "Захист України (д) | Інформатика (хл) "
tu2 = "Російська мова"
tu3 = "Хімія"
tu4 = "Алгебра"
tu5 = "Географія"
tu6 = "Німецька мова"
tu7 = "Українська мова"
tu8 = "Фізкультура"

date3 = env.str("dateWe")
we1 = "Фізкультура"
we2 = "Фізика"
we3 = "Фізика"
we4 = "Біологія"
we5 = "Українська л-ра"
we6 = "Англійська мова"
we7 = "Громадянська освіта"

date4 = env.str("dateTh")
th1 = "Геометрія"
th2 = "Мистецтво"
th3 = "Фізика"
th4 = "Українська мова"
th5 = "Географія"
th6 = "Всесвітня історія"
th7 = "Громадянська освіта"

date5 = env.str("dateFr")
fr1 = "Німецька мова"
fr2 = "Історія України"
fr3 = "Всесвітня історія"
fr4 = "Біологія"
fr5 = "Біологія|Хімія"
fr6 = "Російська мова"
fr7 = "Українська література"