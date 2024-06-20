from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.users import create_new_user, get_all_users
from core.config import settings
from core.models import db_helper
from core.models.user import User
from core.schemas.user import CreateUser, ReadUser
from core.schemas.token import TokenInfo

from core.auth.password import hash_password
from core.auth.login import validate_auth_user
from core.auth.jwt_token import encode_jwt

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("/", response_model=list[ReadUser])
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    users = await get_all_users(session=session)
    return users


@router.post("/", response_model=CreateUser)
async def create_user(
    user_create: CreateUser,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> User:
    user_create.hashed_password = hash_password(user_create.hashed_password)
    user = await create_new_user(user_create=user_create, session=session)
    return user


@router.post("/login/", response_model=TokenInfo)
def auth_user_jwt(user: ReadUser = Depends(validate_auth_user)):
    token = encode_jwt(...)
    return TokenInfo(access_token=token, token_type="Bearer")
