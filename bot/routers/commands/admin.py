from sqlalchemy.ext.asyncio import AsyncSession

from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
from aiogram.filters import Command

from states.admin import NewsletterState

from crud import user as user_crud

from filters import IsAdminFilter

import asyncio

router = Router(name=__name__)
router.message.filter(IsAdminFilter())


@router.message(Command("newsletter"))
async def newsletter(message: types.Message, state: FSMContext):
    await state.set_state(NewsletterState.message)
    await message.answer("Отправь сообщение которое будет разослано всем")


@router.message(NewsletterState.message, F.text)
async def newsletter_message(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
):
    await message.answer("Идет рассылка...")
    for user in await user_crud.get_all_users(session):
        try:
            await message.send_copy(chat_id=user.tg_id)
            await asyncio.sleep(0.2)
        except Exception as ex:
            print(ex)
    await message.answer("Рассылка завершена")
    await state.clear()
