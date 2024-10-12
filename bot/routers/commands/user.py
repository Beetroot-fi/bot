from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram.filters import CommandStart
from aiogram import Router, types

from sqlalchemy.ext.asyncio import AsyncSession

from crud import user as user_crud

router = Router(name=__name__)


@router.message(CommandStart())
async def start_cme(message: types.Message, session: AsyncSession):
    user = await user_crud.get_user_by_tg_id(session, message.from_user.id)
    if not user:
        await user_crud.create_user(session, message.from_user.id)
    try:
        tg_id = int(decode_payload(message.text.split("/start")[1].strip()))
        if tg_id != message.from_user.id and user.referral_id is None:
            await user_crud.update_user(
                session=session,
                tg_id=message.from_user.id,
                referral_id=tg_id,
            )
    except ValueError:
        pass
    ref_link = await create_start_link(
        bot=message.bot,
        payload=str(message.from_user.id),
        encode=True,
    )
    await message.answer(
        text=(
            "Beetroot Finance is an automated yield farming aggregator on TON blockchain 💎"
            "\n\nMaximize your earnings and sleep tight 👇🏼"
            f"\n\nYour referral link <code>\n{ref_link}</code>"
        ),
    )
