from aiogram.fsm.state import State, StatesGroup


class GettingWalletAddressState(StatesGroup):
    wallet_address = State()


class GettingReportMessageState(StatesGroup):
    report_msg = State()
