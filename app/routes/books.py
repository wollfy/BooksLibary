from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import BookModel
from app.schemas import BookSchema, BookGetSchema
from app.database import get_session
from typing import Annotated
router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_session)]

@router.post("/books", response_model=BookSchema)
async def post_book(book: BookSchema, session: SessionDep) -> BookSchema:
    new_book = BookModel(
        title=book.title,
        author=book.author,
        price=book.price,
        amount=book.amount
    )
    session.add(new_book)
    await session.commit()
    return book

@router.get("/books", response_model=list[BookGetSchema])
async def get_books(session: SessionDep) -> list[BookGetSchema]:
    query = select(BookModel)
    result = await session.execute(query)
    books = result.scalars().all()
    return books

@router.put("/books/{book_id}", response_model=BookSchema)
async def update_book(book_id: int, book: BookSchema, session: SessionDep) -> BookSchema:

    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    existing_book = result.scalar_one_or_none()

    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.price = book.price
    existing_book.amount = book.amount

    await session.commit()
    return existing_book

@router.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int, session: SessionDep) -> dict:
    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    existing_book = result.scalar_one_or_none()

    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    await session.delete(existing_book)
    await session.commit()
    return {"detail": "Book deleted successfully"}