from states.user import GettingWalletAddressState, GettingReportMessageState

from pytoniq_core import Address, AddressError

from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types

from core.config import settings

from redis.asyncio import Redis

router = Router(name=__name__)


@router.message(GettingWalletAddressState.wallet_address, F.text)
async def get_user_wallet_address(message: types.Message, state: FSMContext, r: Redis):
    address = message.text
    try:
        address = Address(address)
        await r.sadd(
            "addresses",
            address.to_str(),
        )
        await state.clear()
        await message.answer("Your wallet address add in queue, wait a bit")
    except AddressError:
        await message.answer("Wrong Address!")


@router.message(GettingReportMessageState.report_msg, F.text)
async def get_report_msg(message: types.Message, state: FSMContext):
    for admin in settings.admins:
        await message.bot.send_message(
            chat_id=admin,
            text=f"reported from @{message.from_user.username}\n\ntext:\n{message.text}",
        )
    await message.answer("thanks for report")
    await state.clear()
