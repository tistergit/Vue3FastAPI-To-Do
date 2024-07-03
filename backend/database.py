# from typing import AsyncGenerator

# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# from backend.config import settings

# DATABASE_URL = settings.DATABASE_URL or (
#     f"postgresql+asyncpg://"
#     f"{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
# )

# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

# from ..config import settings

engine = create_async_engine("mysql+aiomysql://root:password@localhost:3306/pet?charset=utf8mb4")
factory = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise
