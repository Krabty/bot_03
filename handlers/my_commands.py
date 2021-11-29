from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline import *


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")


@dp.message_handler(commands="help")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/weather - Вывести погоду"
            )

    await message.answer("\n".join(text))


@dp.message_handler(commands=['menu'])
async def show_menu(message):
    await message.answer(text="Выбери категорию", reply_markup=category_menu)


@dp.callback_query_handler(text="cancel")
async def cancel_button(call: CallbackQuery):
    await call.answer("Ну как хочешь", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text=['category_01'])
async def show_menu_01(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=category_menu_01)
