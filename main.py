from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes import users, documents
import os

app = FastAPI()

# MongoDB connection setup
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["AcademicDocumentationCenter"]

# Include the routers for different resources
app.include_router(users.router)
app.include_router(documents.router)
