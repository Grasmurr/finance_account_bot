from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from handlers.service_backends import get_user_id, Keyboards
from handlers.text_backends import *
from handlers.states import *

from service.users import UserRepository

from database import SessionLocal

from service.users import UserService


@dp.message_handler(commands=['start'])
async def start_message(message: Message, state: FSMContext):
    user_id, chat_id = get_user_id(message)

    user_service = UserService(UserRepository(SessionLocal()))
    user_service.get_or_create_user(user_id, message.from_user.username, message.from_user.full_name)

    markup = Keyboards.create_keyboard_markup('Добавить трату', 'Добавить категорию',
                                              'Статистика и настройки', 'Поддержка')

    await bot.send_photo(chat_id, caption=greeting_text, reply_markup=markup,
                         photo=photo_ids['greeting_photo'])
    await state.set_state(MainMenuStates.initial)


@dp.message_handler(state=MainMenuStates.initial)
async def main_menu_handlers(message: Message, state: FSMContext):
    req = message.text

    if req == 'Добавить трату':
        pass
    elif req == 'Добавить категорию':
        pass
    elif req == 'Статистика и настройки':
        pass
    else:
        pass


@dp.message_handler(content_types=['photo'])
async def return_photo_id(message: Message):
    photo_id = message.photo[-1].file_id
    await message.reply(f'Photo ID: {photo_id}')
