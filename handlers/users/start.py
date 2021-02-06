from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import Message
from keyboards.default.menu import menu_main, menu_class

from loader import dp


@dp.message_handler(CommandStart())
async def show_menu(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Добро пожаловать в NAME_BOT, что бы получить справку нажми на кнопку ПОМОЩЬ.", reply_markup=menu_main)


@dp.message_handler(Text(equals=["Выбрать класс"]))
async def show_menu(message: Message):
    await message.answer(f"Выберите класс.", reply_markup=menu_class)

