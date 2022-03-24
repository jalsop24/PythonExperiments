
import unittest

import UnitTesting.models as models
import UnitTesting.db_process as db_process

class RealDB(unittest.TestCase):

    def test_creation(self):
        models.base.metadata.drop_all(db_process.engine)
        models.base.metadata.create_all(db_process.engine)

if __name__ == "__main__":
    unittest.main()
