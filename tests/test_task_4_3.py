import unittest
import init_test
from ecm.lab_4.task_4_3 import NaiveBubbleSort

class test_Task_3(unittest.TestCase):

    def test_1(self):
        iter = [10, -3, 8, 56]
        self.assertEqual(NaiveBubbleSort(iter), [-3, 8, 10, 56])

    def test_2(self):
        iter = [11, 1000, -7, 18]
        self.assertEqual(NaiveBubbleSort(iter), [-7, 11, 18, 1000])

    def test_3(self):
        iter = [2, 1, 2, 1]
        self.assertEqual(NaiveBubbleSort(iter), [1, 1, 2, 2])

    def test_4(self):
        iter = []
        self.assertEqual(NaiveBubbleSort(iter), [])

    def test_5(self):
        iter = [1, 2, 3, 4, 5]
        self.assertEqual(NaiveBubbleSort(iter), [1, 2, 3, 4, 5])

    def test_6(self):
        iter = [1]
        self.assertEqual(NaiveBubbleSort(iter), [1])

    def test_7(self):
        iter = "aboba <3"
        self.assertRaises(TypeError, NaiveBubbleSort, iter)

    def test_8(self):
        iter = ["MeAbobus", 1, 2, object]
        self.assertRaises(TypeError, NaiveBubbleSort, iter)

    def test_9(self):
        iter = [5, 4, 3, 2, 1]
        self.assertEqual(NaiveBubbleSort(iter), [1, 2, 3, 4, 5])

    def test_10(self):
        iter = [1, 2, "aaa", None]
        self.assertRaises(TypeError, NaiveBubbleSort, iter)

if __name__ == "__main__":
    unittest.main()