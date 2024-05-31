from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import UniqueConstraint

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    active_user: Mapped[bool] = mapped_column()

    __table_args__ = tuple(UniqueConstraint("username", "active_user"))
