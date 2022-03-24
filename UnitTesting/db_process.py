
from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine

from UnitTesting.models import Product, base

engine = create_engine("postgresql+psycopg2://test_account:psql_password@localhost:5432/testing")

def refresh_table():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)


def add_products(product_names):
    with Session(engine) as session, session.begin():
        session: Session

        products = []

        for name in product_names:
            products.append(Product(
                name=name,
                fresh=True
            ))

        session.add_all(products)

def list_products():
    with Session(engine) as session:
        print(session.query(Product).all())

def get_products():
    with Session(engine) as session:
        return {*session.query(Product).all()}

def main():
    refresh_table()
    add_products(["orange", "apple", "pear"])
    list_products()
    

if __name__ == "__main__":
    main()