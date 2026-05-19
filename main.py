from fastapi import FastAPI

from src.api.auth import router as auth_router
from src.api.contacts import router as contacts_router
from src.api.users import router as users_router
from src.database import init_db


def create_app() -> FastAPI:
    app = FastAPI(
        title="Contacts API",
        version="0.1.0",
        description="REST API для зберігання та управління контактами.",
    )

    app.include_router(auth_router, prefix="/api")
    app.include_router(contacts_router, prefix="/api")
    app.include_router(users_router, prefix="/api")

    @app.on_event("startup")
    async def on_startup() -> None:
        # Створюємо таблиці (для домашнього завдання цього достатньо).
        # У реальних проєктах зазвичай використовують міграції (Alembic).
        await init_db()

    return app


app = create_app()

