# app/routes/documents.py

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional, List
from app.models.document import Document
from app.database.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.post("/documents/", response_model=Document)
async def create_document(document: Document, db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Create a new document.

    This endpoint allows users to create a new document by providing details like
    title, description, author, department, and other metadata.
    """
    document_data = document.model_dump()
    await db["documents"].insert_one(document_data)
    return document

@router.get("/documents/", response_model=List[Document])
async def get_documents(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Retrieve a list of documents.

    This endpoint returns a paginated list of documents.
    Use `skip` to indicate the number of documents to skip and `limit` to specify the number of documents to retrieve.
    """
    documents = await db["documents"].find().skip(skip).limit(limit).to_list(limit)
    return documents
