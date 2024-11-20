from states.user import GettingReportMessageState

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

    text = (
        "Beetroot Finance is an automated yield farming aggregator on TON blockchain 💎"
        "\n\nFollow @BeetrootFinance"
    )
    reply_markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Launch",
                    web_app=types.WebAppInfo(url="https://app.beetroot.finance/"),
                )
            ]
        ]
    )

    msg = await message.answer(text=text, reply_markup=reply_markup)

    await message.bot.pin_chat_message(
        chat_id=message.chat.id,
        message_id=msg.message_id,
        disable_notification=True,
    )


@router.message(Command("report"))
async def report(message: types.Message, state: FSMContext):
    await state.set_state(GettingReportMessageState.report_msg)
    await message.answer(text="write a report text")
