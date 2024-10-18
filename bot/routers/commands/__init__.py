__all__ = ("router",)

from .admin import router as admin_router
from .user import router as user_router

from aiogram import Router

router = Router(name=__name__)
router.include_router(user_router)
router.include_router(admin_router)
