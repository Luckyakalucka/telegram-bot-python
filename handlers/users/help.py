from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu_back, menu_main
from loader import dp


@dp.message_handler(Text(equals=["ПОМОЩЬ", "/help"]))
async def show_menu(message: Message):
    await message.answer(f"ТЕКС ХЕЛПА", reply_markup=menu_back)

    @dp.message_handler(Text(equals=["🔙"]))
    async def get_food(message: Message):
        await message.answer("ОК", reply_markup=menu_main)
