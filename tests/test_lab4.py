import unittest
import init_test

class test(unittest.TestCase):

    def test_SelectSort(self):
        from ecm.lab_4.task_4_1 import SelectSort

        #Positive tests
        self.assertEqual(SelectSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])

        #Close to lose tests
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])

        #Special conditions test
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])

        #Negative tests
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([]), [])

    def test_InsertSort(self):
        from ecm.lab_4.task_4_2 import InsertSort

        #Positive tests
        self.assertEqual(InsertSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])

        #Close to lose tests
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])

        #Special conditions test
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])

        #Negative tests
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([]), [])

    def test_NaiveBubbleSort(self):
        from ecm.lab_4.task_4_3 import NaiveBubbleSort

        #Positive tests
        self.assertEqual(NaiveBubbleSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])

        #Close to lose tests
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])

        #Special conditions test
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])

        #Negative tests
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([]), [])

if __name__ == "__main__":
    unittest.main()