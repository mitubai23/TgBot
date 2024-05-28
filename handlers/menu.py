from aiogram import Router, types, F
from aiogram.filters import Command

menu_router = Router()

@menu_router.callback_query(F.data=="menu")
async def menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Пицца"),
                types.KeyboardButton(text="Супы")
            ]
        ]
    )
    await callback.message.answer(f"Наше меню", reply_markup=kb)

@menu_router.message(F.text.lower()=="пицца")
async def pizza(message: types.Message):
    await message.answer(f"Вот пиццы которые мы предлагаем")


@menu_router.message(F.text.lower()=="супы")
async def sup(message: types.Message):
    await message.answer(f"Вот суппы которые мы предлагаем")