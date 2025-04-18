from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///mydb.db"

engine = create_async_engine(DATABASE_URL, echo=True)
new_async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_async_session() as session:
        yield session

class Base(DeclarativeBase):
    pass

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_database():
    # код для закрытия соединений с базой данных
    await engine.dispose()