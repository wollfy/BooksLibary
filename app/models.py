from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    price: Mapped[int]
    amount: Mapped[int]