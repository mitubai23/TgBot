from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await message.answer(f"Ваше имя: {message.from_user.first_name}\n"
                          f"Ваша username: {message.from_user.username}\n"
                          f"Ваш id: {message.from_user.id}")