import unittest
import init_test
from ecm.lab_4.task_4_1 import SelectSort

class test(unittest.TestCase):

    def test_SelectSort(self):
        self.assertEqual(SelectSort([100, 3, -56, 8]), [-56, 3, 8, 100])

if __name__ == "__main__":
    unittest.main()