from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    active_user: bool | None


class UserCreate(UserBase):
    hashed_password: str | None


class UserRead(UserBase):
    id: int
