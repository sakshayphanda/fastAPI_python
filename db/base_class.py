from typing import Any
from sqlalchemy.ext.declarative import as_declarative,declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    def __init__(self):
        print(self, 'constructor')


    @declared_attr
    def __tablename__(self) -> str:
        print(self, 'table name')
        return self.__name__.lower()
