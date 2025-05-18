from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, example="O Auto da Compadecida")
    author: str = Field(..., min_length=3, max_length=100, example="Ariano Suassuna")
    year: int = Field(..., gt=0, example=1995)

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
