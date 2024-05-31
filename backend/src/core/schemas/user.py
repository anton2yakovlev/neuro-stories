from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    active_user: bool


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
