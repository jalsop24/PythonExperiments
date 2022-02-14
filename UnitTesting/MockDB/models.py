
from sqlalchemy import Column, String, Boolean, Integer
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Product(base):

    __tablename__ = "test_products"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    fresh = Column(Boolean)

    def __repr__(self) -> str:
        return f"<{self.id=} {self.name=} {self.fresh=}>"