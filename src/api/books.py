from fastapi import APIRouter
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.data_base import Base, engine
from src.models.books import BookModel
from src.schemas.books import BookSchema, BookGetSchema

router = APIRouter()

@router.post("/")
async def hello_user():
    return {"Сообщение": "Привет друг"}

@router.post("/setup")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@router.post("/books")
async def add_book(book: BookSchema, session: SessionDep) -> BookSchema:
    new_book = BookModel(
        title=book.title,
        author=book.author,
    )
    session.add(new_book)
    await session.commit()
    return book


@router.get("/books")
async def get_books(session: SessionDep) -> list[BookGetSchema]:
    query = select(BookModel)
    result = await session.execute(query)
    books = result.scalars().all()
    print(f"{books=}")
    return books