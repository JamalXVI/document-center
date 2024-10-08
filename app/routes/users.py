# app/routes/users.py

from fastapi import APIRouter, Depends
from app.models.user import User
from app.database.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: User, db: AsyncIOMotorDatabase = Depends(get_database)):
    user_data = user.model_dump()
    await db["users"].insert_one(user_data)
    return user