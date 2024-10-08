import asyncio
from app.database.database import get_database
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_default_admin():
    db = await get_database()
    existing_admin = await db["users"].find_one({"username": "admin"})
    if not existing_admin:
        default_admin = {
            "username": "admin",
            "password_hash": pwd_context.hash("admin"),
            "role": "admin"
        }
        await db["users"].insert_one(default_admin)

# Run the create_default_admin function at startup
@app.on_event("startup")
async def startup_event():
    await create_default_admin()
