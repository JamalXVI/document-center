from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class Document(BaseModel):
    title: str
    description: Optional[str]
    author: Optional[str]
    department: Optional[str]
    publication_date: Optional[str]
    document_type: str
    file_path: str
    created_by: Optional[int]

@router.post("/documents/")
async def create_document(document: Document):
    document_data = document.dict()
    await db["documents"].insert_one(document_data)
    return document

@router.get("/documents/", response_model=List[Document])
async def get_documents():
    documents = await db["documents"].find().to_list(100)
    return documents
