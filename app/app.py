from fastapi import FastAPI,HTTPException,File,UploadFile,Depends,Form
from app.schemas import PostCreate,PostResponse
from app.db import Post,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app=FastAPI(lifespan=lifespan)

