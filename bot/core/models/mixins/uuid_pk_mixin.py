from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID as PYUUID
from uuid import uuid4


class UuidPkMixin:
    id: Mapped[PYUUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )