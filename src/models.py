from datetime import date

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовий клас для ORM-моделей."""


class Contact(Base):
    """Модель контакту."""

    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)

    birthday: Mapped[date] = mapped_column(Date, nullable=False)

    # Додаткові дані — довільний текст (необовʼязково)
    extra: Mapped[str | None] = mapped_column(Text, nullable=True)

