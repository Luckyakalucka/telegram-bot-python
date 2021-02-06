from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu_class, menu_main
from loader import dp


@dp.message_handler(Text(equals=["/setclass", "Класс"]))
async def show_menu(message: Message):
    await message.answer(f"Выбрын {message.text} класс. Выберите День недели", reply_markup=menu_class)


@dp.message_handler(Text(equals=["🔙"]))
async def get_food(message: Message):
    await message.answer("ОК", reply_markup=menu_main)