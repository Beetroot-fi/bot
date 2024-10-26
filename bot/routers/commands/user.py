from utils.ref_link import create_ref_link

from aiogram.filters import CommandStart
from aiogram import Router, types

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
                        text="launch",
                        web_app=types.WebAppInfo(url="https://app.beetroot.finance"),
                    )
                ]
            ]
        ),
    )
