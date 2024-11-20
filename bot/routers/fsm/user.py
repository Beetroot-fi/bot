from states.user import GettingReportMessageState

from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types

from core.config import settings

router = Router(name=__name__)


@router.message(GettingReportMessageState.report_msg, F.text)
async def get_report_msg(message: types.Message, state: FSMContext):
    for admin in settings.admins:
        await message.bot.send_message(
            chat_id=admin,
            text=f"reported from @{message.from_user.username}\n\ntext:\n{message.text}",
        )
    await message.answer("thanks for report")
    await state.clear()
