from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        unique=True,
        autoincrement=True,
    )
    uuid: Mapped[str] = mapped_column(String(36))
    name_first: Mapped[str] = mapped_column(String(30))
    name_last: Mapped[str] = mapped_column(String(30))
    name_middle: Mapped[str] = mapped_column(String(10))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))
