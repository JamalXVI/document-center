from fastapi import APIRouter, Depends
from app.models.user import User
from app.database.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from passlib.context import CryptContext

router = APIRouter()

# Password hashing utility
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/users/", response_model=User)
async def create_user(user: User, db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Create a new user.

    This endpoint allows the creation of a new user with fields like username, password hash, and role.
    """
    user_data = user.dict()
    user_data['password_hash'] = get_password_hash(user.password_hash)  # Hash the password before saving
    await db["users"].insert_one(user_data)
    return user
