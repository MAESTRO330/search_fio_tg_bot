"""
Хендлер с вопросом
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_questions import get_yes_no_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """
    Ответ на команду старт
    """
    await message.answer(
        "Вы довольны своей работой?",
        reply_markup=get_yes_no_kb()
    )


@router.message(F.text.lower() == "да")
async def answer_yes(message: Message):
    """
    Ответ на кнопку да
    """
    await message.answer(
        "Это здорово",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.loewr() == "нет")
async def answer_no(message: Message):
    """
    Ответ на кнопку нет
    """
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )
