from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from environs import Env

from keyboards.default import menu_day_11, menu_class
from loader import dp


@dp.message_handler(Text(equals=["11"]))
async def show_menu(message: Message):
    await message.answer(f"Выбрын {message.text} класс. Выберите День недели", reply_markup=menu_day_11)

    # @dp.message_handler(Text(equals=["11 класс"]))
    # async def get_food(message: Message):
    #   await message.answer(f"Вы выбрали {message.text}. Выберите день недели", reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟠 Понедельник 🟠"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Понедельник для 11 класса:\n"
                             f"Дата: {date1}\n"
                             f"1. {mo1}\n"
                             f"2. {mo2}\n"
                             f"3. {mo3}\n"
                             f"4. {mo4}\n"
                             f"5. {mo5}\n"
                             f"6. {mo6}\n"
                             f"7. {mo7}\n",
                             reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟠 Вторник 🟠"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Вторник для 11 класса:\n"
                             f"Дата: {date2}\n"
                             f"1. {tu1}\n"
                             f"2. {tu2}\n"
                             f"3. {tu3}\n"
                             f"4. {tu4}\n"
                             f"5. {tu5}\n"
                             f"6. {tu6}\n"
                             f"7. {tu7}\n"
                             f"8. {tu8}\n",
                             reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟠 Среда 🟠"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Среду для 11 класса:\n"
                             f"Дата: {date3}\n"
                             f"1. {we1}\n"
                             f"2. {we2}\n"
                             f"3. {we3}\n"
                             f"4. {we4}\n"
                             f"5. {we5}\n"
                             f"6. {we6}\n"
                             f"7. {we7}\n"
                             f"7. {we8}\n",
                             reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟠 Четверг 🟠"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Четверг для 11 класса:\n"
                             f"Дата: {date4}\n"
                             f"1. {th1}\n"
                             f"2. {th2}\n"
                             f"3. {th3}\n"
                             f"4. {th4}\n"
                             f"5. {th5}\n"
                             f"6. {th6}\n"
                             f"7. {th7}\n",
                             reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["🟠 Пятница 🟠"]))
    async def get_food(message: Message):
        await message.answer(f"Вот что мне удалось найти на Пятницу для 11 класса:\n"
                             f"Дата: {date5}\n"
                             f"1. {fr1}\n"
                             f"2. {fr2}\n"
                             f"3. {fr3}\n"
                             f"4. {fr4}\n"
                             f"5. {fr5}\n"
                             f"6. {fr6}\n"
                             f"7. {fr7}\n",
                             reply_markup=menu_day_11)

    @dp.message_handler(Text(equals=["/setclass", "Выбрать другой класс"]))
    async def show_menu(message: Message):
        await message.answer(f"Выберите класс", reply_markup=menu_class)


env = Env()
env.read_env()

date1 = env.str("dateMo")
mo1 = "Англійська мова"
mo2 = "Фізкультура"
mo3 = "Всесвітня історія"
mo4 = "Українська література"
mo5 = "Геометрія"
mo6 = "Історія України"
mo7 = "Всесвітня історія"

date2 = env.str("dateTu")
tu1 = "Фізика"
tu2 = "Захист України (д) | Інформатика (хл)"
tu3 = "Українська мова"
tu4 = "Географія"
tu5 = "Фізика"
tu6 = "Хімія"
tu7 = "Історія України"
tu8 = "Фізкультура"

date3 = env.str("dateWe")
we1 = "Історія України"
we2 = "Мистецтво"
we3 = "Російська мова"
we4 = "Українська література"
we5 = "Англійська мова"
we6 = "Геометрія"
we7 = "Біологія/екологія"
we8 = "Фізкультура"

date4 = env.str("dateTh")
th1 = "Фізика"
th2 = "Фізика"
th3 = "Українська мова"
th4 = "Російська мова"
th5 = "Алгебра"
th6 = "Англійська мова"
th7 = ""
th8 = ""

date5 = env.str("dateFr")
fr1 = "Зарубіжна література"
fr2 = "Хімія"
fr3 = "Захист України"
fr4 = "Інформатика (д) | Захист України (хл)"
fr5 = "Алгебра"
fr6 = "Біологія"
fr7 = "Всесвітня історія | -"