from fastapi import FastAPI, Request, status
from slowapi.errors import RateLimitExceeded
from starlette.responses import JSONResponse

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

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"error": "Too many requests. Please try again later."},
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

