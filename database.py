import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "employee_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "admin")
DB_PORT = os.getenv("DB_PORT", "5433")
POOL_SIZE = os.getenv("POOL_SIZE", 5)
MAX_OVER_FLOW = os.getenv("MAX_OVER_FLOW", 10)

#postgres database url
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# create engine
engine = create_async_engine(DATABASE_URL,pool_size=int(POOL_SIZE), max_overflow=int(MAX_OVER_FLOW),echo=False)

async_session= async_sessionmaker(
    engine, class_=AsyncSession,expire_on_commit=False,autocommit=False,autoflush=False)

base = declarative_base()

# get_session
async def get_session() -> AsyncGenerator[AsyncSession, None]: #Generator function

    async with async_session() as session:
        yield session


async def init_db() -> None:

    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

async def close_db() -> None:
    await engine.dispose()
