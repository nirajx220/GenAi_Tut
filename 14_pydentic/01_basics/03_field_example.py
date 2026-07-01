from pydantic import BaseModel
from typing import Optional, List, Dict

class Cart(BaseModel):
    user_id: int
    items: List[str] 
    quantity: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str 
    images: Optional[List[str]] = None  # Optional field with default value None   