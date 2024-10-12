from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger

from .mixins import UuidPkMixin
from .base import Base


class User(Base, UuidPkMixin):
    tg_id: Mapped[int] = mapped_column(BigInteger)
    referral_id: Mapped[int | None] = mapped_column(BigInteger)
