from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
