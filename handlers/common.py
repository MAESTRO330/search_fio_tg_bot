"""
Общий файл с базовымы обработчиками
"""

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove


router = Router()


class GroupList(StatesGroup):
    """
    Класс с состояниями для работы со списком группы
    """
    waiting_group_list = State()
    update_group_list = State()


@router.message(Command(commands=['start']))
async def cmd_start(message: Message, state: FSMContext):
    """
    Функция обработчик, отвечающая на команду старт
    """
    await state.clear()
    await message.answer(
        text="Привет, этот бот создан для поиска фамилий по списку\n\n"
        "Отправь мне список группы файлом excel, чтоб я мог сверять фамилии с ним",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(GroupList.waiting_group_list)


@router.message(
    GroupList.waiting_group_list,
    F.document
)
async def first_upload_group_list(message: Message, state: FSMContext):
    """
    Функция обработчик принимающая список группы при запуске бота
    """
    pass
