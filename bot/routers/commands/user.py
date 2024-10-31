from states.user import GettingWalletAddressState

from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, types


router = Router(name=__name__)


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    try:
        chat = await message.bot.get_chat(message.chat.id)
        if chat.pinned_message:
            await message.bot.unpin_chat_message(
                chat_id=message.chat.id,
                message_id=chat.pinned_message.message_id,
            )
    except TelegramBadRequest:
        pass

    msg = await message.answer(
        text=(
            "Beetroot Finance is an automated yield farming aggregator on TON blockchain 💎"
            "\n\nFollow @BeetrootFinance"
            f"\n\nTo get TESTNET USDT send /get"
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

    await message.bot.pin_chat_message(
        chat_id=message.chat.id,
        message_id=msg.message_id,
        disable_notification=True,
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
