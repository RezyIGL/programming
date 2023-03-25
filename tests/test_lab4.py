import unittest
import init_test

class test(unittest.TestCase):

    def test_SelectSort(self):
        from ecm.lab_4.task_4_1 import SelectSort
        self.assertEqual(SelectSort([100, 3, -56, 8]), [-56, 3, 8, 100])

    def test_InsertSort(self):
        from ecm.lab_4.task_4_2 import InsertSort
        self.assertEqual(InsertSort([100, 3, -56, 8]), [-56, 3, 8, 100])

if __name__ == "__main__":
    unittest.main()