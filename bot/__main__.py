from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode, ChatType
from aiogram import Bot, Dispatcher

from utils.log import setup_logging

from core.config import settings

from filters import ChatTypeFilter

from routers import router

import asyncio
import logging


async def main():
    """Main entrypoint"""

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
    setup_logging(level=logging.WARNING)
    asyncio.run(main())
