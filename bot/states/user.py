from aiogram.fsm.state import State, StatesGroup


class GettingReportMessageState(StatesGroup):
    report_msg = State()
