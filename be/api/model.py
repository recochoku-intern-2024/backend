from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from db import Base
from db import ENGINE

# テーブル定義
class TestUserTable(Base):
    __tablename__ = 'test_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)

# class TestUserPostTable(Base):
#     __tablename__ = 'test_user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(30), nullable=False)
#     email = Column(String(128), nullable=False)


class KyakuhonTable(Base):
    __tablename__ = 'kyakuhon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    author = Column(String(30), nullable=False)
    genre = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


# モデル定義 
class TestUser(BaseModel):
    id: int
    name: str
    email: str

class Kyakuhon(BaseModel):
    id: int
    title: str
    author: str
    genre: int
    price: int

class KyakuhonPost(BaseModel):
    title: str
    author: str
    genre: int
    price: int


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()

