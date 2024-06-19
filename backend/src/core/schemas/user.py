from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class BaseUser(BaseModel):
    model_config = ConfigDict(strict=True)

    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr | None = None


class CreateUser(BaseUser):
    hashed_password: str | bytes


class ReadUser(BaseUser):
    id: int
    active: bool = True
