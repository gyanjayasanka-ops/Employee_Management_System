from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine, init_db, close_db
from routers import router as employee_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield
    await close_db()

app = FastAPI(title="Employee Management API",lifespan=lifespan)

app.include_router(employee_router)