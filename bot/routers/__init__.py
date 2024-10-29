__all__ = ("router",)

from .commands import router as commands_router
from .fsm import router as fsm_router

from aiogram import Router

router = Router(name=__name__)
router.include_router(commands_router)
router.include_router(fsm_router)
