from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatType
from aiogram import Bot, Dispatcher

from filters import ChatTypeFilter

from core.config import settings

from routers import router

import asyncio
import logging


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True,
        ),
    )

    dp = Dispatcher()
    dp.include_router(router)
    dp.message.filter(ChatTypeFilter(chat_types=[ChatType.PRIVATE]))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    asyncio.run(main())
