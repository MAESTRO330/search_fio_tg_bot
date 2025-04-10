"""
Файл с логикой поиска фамилий
"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from common import GroupList

router = Router()

async def excel_to_db():
    pass