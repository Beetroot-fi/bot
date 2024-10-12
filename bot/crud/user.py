from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from core.models import User


async def create_user(session: AsyncSession, tg_id: int) -> User:
    user = User(tg_id=tg_id)

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def get_user_by_tg_id(session: AsyncSession, tg_id: int) -> User | None:
    return await session.scalar(select(User).where(User.tg_id == tg_id))


async def update_user(session: AsyncSession, tg_id: int, **kwargs) -> None:
    await session.execute(update(User).where(User.tg_id == tg_id).values(**kwargs))
    await session.commit()


async def delete_user(session: AsyncSession, tg_id: int) -> None:
    await session.execute(delete(User).where(User.tg_id == tg_id))
    await session.commit()
