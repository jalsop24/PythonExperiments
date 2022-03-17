
from sqlalchemy import text
import sqlalchemy
from sqlalchemy.engine import create_engine

engine = create_engine("postgresql+psycopg2://test_account:psql_password@localhost:5432/testing", echo=True)

def insert_products():
    with engine.begin() as connection:
        connection: sqlalchemy.engine.Connection
        
        connection.execute(text(
        '''
        insert into test_products (name, fresh)
        values (:name, :fresh)
        '''),
        [{"name": "bannanana", "fresh": True}, {"name": "peas", "fresh": True}]
        )

def update_products(ids: list):
    with engine.begin() as connection:
        connection: sqlalchemy.engine.Connection
        
        connection.execute(text(
        '''
        update test_products
        set "fresh" = :fresh
        where "id" = :id
        '''),
        [{"fresh": False, "id": _id} for _id in ids]
        )


def main():
    update_products([1, 2, 4, 8])
    

if __name__ == "__main__":
    main()
