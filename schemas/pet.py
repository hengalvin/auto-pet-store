from pydantic import BaseModel
from typing import Optional, List


class Category(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Tag(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class PetResponse(BaseModel):
    id: Optional[int]
    category: Optional[Category] = None
    name: Optional[str] = None
    photoUrls: List[str] = None
    tags: Optional[List[Tag]] = None
    status: Optional[str]  = None # enum: available, pending, sold