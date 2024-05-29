from aiogram import Router, F, types
from aiogram.filters import Command
from config import database
from pprint import pprint

menu_router = Router()

@menu_router.callback_query(F.data=="menu")
async def menu(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Пицца"),
                types.KeyboardButton(text="Супы")
            ],
            [
                types.KeyboardButton(text="Роллы")
            ]
        ]
    )
    await callback.message.answer(f"Наше меню", reply_markup=kb)

book_genres = ("пицца", "супы", "роллы")


@menu_router.message(F.text.lower().in_(book_genres))
async def show_meals(message: types.Message):
    category = message.text
    print("Пользователь нажал на кнопку", category)
    data = await database.fetch(
        """SELECT * FROM meals 
        INNER JOIN categories ON meals.category_id = categories.id 
        WHERE categories.name = ?""",
        (category,)
    )
    pprint(data)
    if not data:
        await message.answer("К сожалению, ничего не нашлось")
        return
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Блюда категории {category}:", reply_markup=kb)
    for meal in data:
        image = types.FSInputFile(meal.get("picture"))
        await message.answer_photo(
            photo=image,
            caption=f"{meal['name']} - {meal['description']}\nЦена: {meal['price']} сом")