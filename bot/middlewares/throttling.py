from aiogram.types import TelegramObject, Message
from aiogram import BaseMiddleware

from typing import Callable, Awaitable, Any

from redis.asyncio import Redis


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis):
        self.redis = redis

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        user = f"user:{event.from_user.id}"

        check_user = await self.redis.get(name=user)

        if check_user:
            if int(check_user) == 1:
                await self.redis.set(name=user, value=0, ex=60)
                return await event.answer(text="Stop spam, mute for 1 minute.")
            return

        await self.redis.set(name=user, value=1, ex=60)

        return await handler(event, data)
