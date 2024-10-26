from base64 import urlsafe_b64encode

from aiogram import Bot


def _encode_payload(payload: str) -> str:
    """Encoding some payload"""

    bytes_payload: bytes = urlsafe_b64encode(payload.encode("utf-8"))
    str_payload = bytes_payload.decode()
    return str_payload.replace("=", "")


async def create_ref_link(bot: Bot, payload: str, app_name: str) -> str:
    """Getting startapp link"""

    payload = _encode_payload(payload)
    bot_username = (await bot.get_me()).username
    return f"https://t.me/{bot_username}/{app_name}?startapp={payload}"
