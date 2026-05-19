from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.repository.users import UsersRepository
from src.schemas import UserCreate, UserResponse
from src.services.passwords import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(body: UserCreate, db: AsyncSession = Depends(get_db)):
    repo = UsersRepository(db)

    if await repo.exists_by_email_or_username(email=body.email, username=body.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email or username already exists",
        )

    user = await repo.create(body, hashed_password=hash_password(body.password))
    return user

