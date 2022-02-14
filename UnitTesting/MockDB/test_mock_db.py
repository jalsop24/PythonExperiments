
import unittest
from unittest.mock import patch

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from models import Product, base

import db_process

class DBTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///:memory:")

        base.metadata.drop_all(cls.engine)
        base.metadata.create_all(cls.engine)

    def test_session(self):
        with patch("db_process.Session") as mock_session:
            mock_session.return_value = Session(self.engine)
            
            product_names = {"lolipop", "bear", "ant"}
            
            db_process.add_products(product_names)

            products = db_process.get_products()

            self.assertEqual(product_names, {product.name for product in products})


if __name__ == "__main__":
    unittest.main()
