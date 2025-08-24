from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=1000)
    author: str = Field(..., min_length=1, max_length=1000)
    year: int = Field(..., gt=1900, lt=2100)

class BookResponse(BaseModel):
    title: str
    author: str