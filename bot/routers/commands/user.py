from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, types

from states.user import GettingWalletAddressState

from utils.ref_link import create_ref_link

router = Router(name=__name__)


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    ref_link = await create_ref_link(
        bot=message.bot,
        payload=str(message.from_user.id),
        app_name="BeetrootFi",
    )
    await message.answer(
        text=(
            "Beetroot Finance is an automated yield farming aggregator on TON blockchain 💎"
            "\n\nFollow @BeetrootFinance"
            f"\n\nand invite your friends👇🏼\n<code>{ref_link}</code>"
        ),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="Launch",
                        web_app=types.WebAppInfo(url="https://app.beetroot.finance"),
                    )
                ]
            ]
        ),
    )


@router.message(Command("get"))
async def get_usdt(message: types.Message, state: FSMContext):
    await state.set_state(GettingWalletAddressState.wallet_address)
    await message.answer(
        text=(
            "Enter wallet address (format: raw or base64):"
            "\n\nExample:"
            "\n<code>0QCSES0TZYqcVkgoguhIb8iMEo4cvaEwmIrU5qbQgnN8fo2A</code>"
        )
    )
