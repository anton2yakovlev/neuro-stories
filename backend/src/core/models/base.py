from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import declared_attr
from utils.table_name_formatter import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)
