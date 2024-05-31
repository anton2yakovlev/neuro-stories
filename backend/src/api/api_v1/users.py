from fastapi import APIRouter

from core.config import settings

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get()
async def get_user()