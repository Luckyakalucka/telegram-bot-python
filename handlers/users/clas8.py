from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_8, menu_class
from loader import dp


@dp.message_handler(Text(equals=["8"]))
async def show_menu(message: Message):
    await message.answer(f"Выбран {message.text} класс. Выберите День недели", reply_markup=menu_day_8)

    # @dp.message_handler(Text(equals=["11 класс"]))
    # async def get_food(message: Message):
    #   await message.answer(f"Вы выбрали {message.text}. Выберите день недели", reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟢 Понедельник 🟢"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 8 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_8)

    @dp.message_handler(Text(equals=["🟢 Вторник 🟢"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 8 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n",
                             reply_markup=menu_day_8)

    @dp.message_handler(Text(equals=["🟢 Среда 🟢"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среду для 8 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n"
                             f"8. {we8}\n",
                             reply_markup=menu_day_8)

    @dp.message_handler(Text(equals=["🟢 Четверг 🟢"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 8 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n"
                             f"8. {th8}\n",
                             reply_markup=menu_day_8)

    @dp.message_handler(Text(equals=["🟢 Пятница 🟢"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятницу для 8 класса:"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_8)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)


env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Англійська мова"
mo2 = "Геометрія"
mo3 = "Українська мова"
mo4 = "Фізкультура"
mo5 = "Біологія"
mo6 = "Література"
mo7 = "- | Історія України"

date2 = env.str("dateTu")
tu1 = "Хімія"
tu2 = "Фізика"
tu3 = "Алгебра"
tu4 = "Біологія"
tu5 = "Українська література"
tu6 = "Історія України"
tu7 = "Фізкультура"

date3 = env.str("dateWe")
we1 = "Інформатика (ІІ)"
we2 = "Російська мова"
we3 = "Німецька мова"
we4 = "Геометрія"
we5 = "Географія"
we6 = "Всесвітня історія"
we7 = "Українська мова"
we8= "Інформатика (ІІ)"

date4 = env.str("dateTh")
th1 = "Основи здоров'я"
th2 = "Фізкультура"
th3 = "Англійська мова"
th4 = "Фізика"
th5 = "Російська мова"
th6 = "Трудове навчання"
th7 = "Інформатика (І)"
th8 = "Інформатика (І)"

date5 = env.str("dateFr")
fr1 = "Хімія"
fr2 = "Мистецтво"
fr3 = "Українська література"
fr4 = "Алгебра"
fr5 = "Німецька мова"
fr6 = "Географія"
fr7 = "Література"