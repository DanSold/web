import datetime

from sqlalchemy import (
    Column, Integer, String, DateTime, Boolean,
    ForeignKey,
)

from database import Base


class BaseInfoMixin:
    id = Column(Integer, primary_key=True)


class User(BaseInfoMixin, Base):
    __tablename__ = 'user'

    name = Column(String, nullable=False)
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    moderator = Column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return f'User {self.name} -> #{self.id}'


class Dish(BaseInfoMixin, Base):
    __tablename__ = 'dish'

    name = Column(String, nullable=False)
    recipe = Column(String, nullable=False)
    author = Column(ForeignKey('user.id'), nullable=False)
    picture = Column(String, nullable=False)
