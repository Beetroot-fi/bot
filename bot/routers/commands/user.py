from aiogram.filters import CommandStart
from aiogram import Router, types

router = Router(name=__name__)


@router.message(CommandStart())
async def start_cme(message: types.Message):
    await message.answer(text="start message")
