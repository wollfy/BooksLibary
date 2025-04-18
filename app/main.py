from fastapi import FastAPI
from app.database import setup_database, close_database
from app.routes.books import router as books_router

app = FastAPI()

@app.lifespan
async def lifespan(app: FastAPI):
    await setup_database()
    yield  # Это указывает на то, что приложение работает

    # Код, который выполняется при завершении работы приложения
    await close_database()  # Закрытие соединений с базой данных, если необходимо

app.include_router(books_router, tags=["books 📚"])