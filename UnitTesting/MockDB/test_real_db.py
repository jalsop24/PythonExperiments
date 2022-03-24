
import unittest

from . import models

class RealDB(unittest.TestCase):

    def test_creation(self):
        models.base.metadata.drop_all()
        models.base.metadata.create_all()

if __name__ == "__main__":
    unittest.main()