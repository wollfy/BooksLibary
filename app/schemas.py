from pydantic import BaseModel, Field

class BookSchema(BaseModel):
    title: str = Field(min_length=3, max_length=20, default="Clean Code")
    author: str = Field(min_length=1, max_length=20, default="Bob Martin")
    price: int = Field(ge=1, description="Цена")
    amount: int

class BookGetSchema(BaseModel):
    id: int
    title: str
    author: str
    price: int
    amount: int