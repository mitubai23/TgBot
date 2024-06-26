from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import database


survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    phone_num = State()
    visit = State()
    rate = State()
    review = State()

@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(BookSurvey.phone_num)
    await message.answer("Ваш номер телефона")

@survey_router.message(BookSurvey.phone_num)
async def process_age(message: types.Message, state: FSMContext):
    phone_num = message.text
    await state.update_data(phone_num=phone_num)
    await state.set_state(BookSurvey.visit)
    await message.answer("Когда вы последний раз были у нас?")

@survey_router.message(BookSurvey.visit)
async def process_gender(message: types.Message, state: FSMContext):
    visit = message.text
    await state.update_data(visit=visit)
    await state.set_state(BookSurvey.rate)
    await message.answer("Оценка нашему ресторану")


@survey_router.message(BookSurvey.rate)
async def process_gender(message: types.Message, state: FSMContext):
    rate = message.text
    await state.update_data(rate=rate)
    await state.set_state(BookSurvey.review)
    await message.answer("Оставьте ваш отызв")

@survey_router.message(BookSurvey.review)
async def process_genre(message: types.Message, state: FSMContext):
    review = message.text
    await state.update_data(review=review)
    await message.answer(f"Спасибо за прохождение опроса, {message.from_user.full_name}!")
    data = await state.get_data()
    await database.execute( "INSERT INTO surveys (name, phone_num, visit, rate, review) VALUES (?, ?, ?, ?, ?)",
                            (data["name"], data["phone_num"], data["visit"], data["rate"], data["review"]),)
    await state.clear()