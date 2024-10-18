from aiogram.filters import Filter
from aiogram import types

from core.config import settings


class IsAdminFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in settings.admins
