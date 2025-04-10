"""
Файл с клавиатурой главного меню
"""

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_kb() -> ReplyKeyboardMarkup:
    """
    Главная клавиатура
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Настройки")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def return_kb() -> ReplyKeyboardMarkup:
    """
    Клавиатура для возврата на главуню
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="На главную")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
