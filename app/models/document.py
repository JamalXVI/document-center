from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    title: str
    description: Optional[str] = None
    author: Optional[str] = None
    department: Optional[str] = None
    publication_date: Optional[str] = None
    document_type: str
    file_path: str
    created_by: Optional[int] = None
    created_at: Optional[str] = None
