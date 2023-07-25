from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, KeyboardButton


def get_user_id(message: Message, call: CallbackQuery = None) -> tuple[int, int]:
    if call:
        return call.from_user.id, call.message.chat.id
    return message.from_user.id, message.chat.id


class Keyboards:
    @staticmethod
    def create_keyboard_markup(*button_names):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in button_names:
            button = KeyboardButton(i)
            markup.add(button)
        return markup

    @staticmethod
    def create_inline_keyboard(*tuples_with_name_and_callback):
        markup = InlineKeyboardMarkup()
        for n, c in tuples_with_name_and_callback:
            button = InlineKeyboardButton(text=n, callback_data=c)
            markup.add(button)
        return markup
