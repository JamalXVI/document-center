# app/routes/documents.py

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional, List
from app.models.document import Document
from app.database.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.post("/documents/", response_model=Document)
async def create_document(document: Document, db: AsyncIOMotorDatabase = Depends(get_database)):
    document_data = document.dict()
    await db["documents"].insert_one(document_data)
    return document

@router.get("/documents/", response_model=List[Document])
async def get_documents(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: AsyncIOMotorDatabase = Depends(get_database)):
    documents = await db["documents"].find().skip(skip).limit(limit).to_list(limit)
    return documents