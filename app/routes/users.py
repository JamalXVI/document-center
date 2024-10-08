from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()

class User(BaseModel):
    username: str
    password_hash: str
    role: str

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["AcademicDocumentationCenter"]

@router.post("/users/")
async def create_user(user: User):
    user_data = user.dict()
    await db["users"].insert_one(user_data)
    return user
