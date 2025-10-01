from typing import Optional
from pydantic import BaseModel, Field

class Bookbase(BaseModel):
    title: str = Field(..., example="Diaro de um Banana")
    author: str = Field(..., example="Jeff Kinney")
    year: Optional[int] = Field(None, example=2007)
    genre: Optional[str] = Field(None, example="Humor")
    
class BookCreate(Bookbase):
    pass

class BookUpdate(Bookbase):
    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = Field(None, ge=1)
    genre: Optional[str] = None
    
class BookOut(Bookbase):
    id: int

    class Config:
        orm_mode = True