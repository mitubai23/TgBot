from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наше меню", callback_data="menu"),
                types.InlineKeyboardButton(text="Наш ватсапп", url="t.me")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)