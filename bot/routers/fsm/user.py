from states.user import GettingWalletAddressState

from pytoniq_core import Address, AddressError

from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types

from redis.asyncio import Redis

router = Router(name=__name__)


@router.message(GettingWalletAddressState.wallet_address, F.text)
async def get_user_wallet_address(
    message: types.Message,
    state: FSMContext,
    r: Redis,
):
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
