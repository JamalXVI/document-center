from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password_hash: str
    role: str
    created_at: Optional[str] = None
