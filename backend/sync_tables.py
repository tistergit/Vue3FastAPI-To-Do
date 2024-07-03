
from sqlalchemy import create_engine

from models import PetUsers,BaseModel
from sqlalchemy.orm import DeclarativeBase


def create_tables():
    engine = create_engine("mysql+pymysql://root:password@localhost:3306/pet?charset=utf8mb4")
    BaseModel.metadata.create_all(engine)

if __name__ == "__main__":
    print("create tables")
    create_tables()
