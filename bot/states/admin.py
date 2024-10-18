from aiogram.fsm.state import StatesGroup, State


class NewsletterState(StatesGroup):
    message = State()
