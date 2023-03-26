import unittest
import init_test

class test(unittest.TestCase):

    def test_SelectSort(self):
        from ecm.lab_4.task_4_1 import SelectSort

        #Positive tests
        self.assertEqual(SelectSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(SelectSort([13, 534, 23, -100]), [-100, 13, 23, 534])
        self.assertEqual(SelectSort([123, 12345, 4235, 62345]), [123, 4235, 12345, 62345])
        self.assertEqual(SelectSort([234, 12]), [12, 234])
        self.assertEqual(SelectSort([10, 9, 4, 2, 5, 3]), [2, 3, 4, 5, 9, 10])
        self.assertEqual(SelectSort([11, 1000, -7, 12]), [-7, 11, 12, 1000])
        self.assertEqual(SelectSort([23, 11, 2, 33]), [2, 11, 23, 33])
        self.assertEqual(SelectSort([123, 110, 124]), [110, 123, 124])
        self.assertEqual(SelectSort([768, 234, 322]), [234, 322, 768])
        self.assertEqual(SelectSort([1337, 228, 993]), [228, 993, 1337])

        #Close to lose tests
        self.assertEqual(SelectSort([]), [])
        self.assertEqual(SelectSort([1]), [1])
        self.assertEqual(SelectSort([2]), [2])
        self.assertEqual(SelectSort([3]), [3])
        self.assertEqual(SelectSort([4]), [4])
        self.assertEqual(SelectSort([5]), [5])
        self.assertEqual(SelectSort([6]), [6])
        self.assertEqual(SelectSort([7]), [7])
        self.assertEqual(SelectSort([8]), [8])
        self.assertEqual(SelectSort([9]), [9])

        #Special conditions test
        self.assertEqual(SelectSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(SelectSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(SelectSort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(SelectSort([2, 1, 3, 2, 1, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(SelectSort([1000, -7, 993, -7, 986, -7]), [-7, -7, -7, 986, 993, 1000])
        self.assertEqual(SelectSort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(SelectSort([1, 2, 2, 1]), [1, 1, 2, 2])
        self.assertEqual(SelectSort([3, 3, 2, 2]), [2, 2, 3, 3])
        self.assertEqual(SelectSort([1, 2, 3, 3, 2, 1]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(SelectSort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

        #Negative tests
        self.assertEqual(SelectSort((11, 22)), [11, 22])
        self.assertEqual(SelectSort("aboba <3"), "A chto tut napisat'?")
        self.assertEqual(SelectSort("ya ghoul, 1000-7"), "Postav'te zachet pojaluysta")

    def test_InsertSort(self):
        from ecm.lab_4.task_4_2 import InsertSort

        self.assertEqual(InsertSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(InsertSort([13, 534, 23, -100]), [-100, 13, 23, 534])
        self.assertEqual(InsertSort([123, 12345, 4235, 62345]), [123, 4235, 12345, 62345])
        self.assertEqual(InsertSort([234, 12]), [12, 234])
        self.assertEqual(InsertSort([10, 9, 4, 2, 5, 3]), [2, 3, 4, 5, 9, 10])
        self.assertEqual(InsertSort([11, 1000, -7, 12]), [-7, 11, 12, 1000])
        self.assertEqual(InsertSort([23, 11, 2, 33]), [2, 11, 23, 33])
        self.assertEqual(InsertSort([123, 110, 124]), [110, 123, 124])
        self.assertEqual(InsertSort([768, 234, 322]), [234, 322, 768])
        self.assertEqual(InsertSort([1337, 228, 993]), [228, 993, 1337])

        self.assertEqual(InsertSort([]), [])
        self.assertEqual(InsertSort([1]), [1])
        self.assertEqual(InsertSort([2]), [2])
        self.assertEqual(InsertSort([3]), [3])
        self.assertEqual(InsertSort([4]), [4])
        self.assertEqual(InsertSort([5]), [5])
        self.assertEqual(InsertSort([6]), [6])
        self.assertEqual(InsertSort([7]), [7])
        self.assertEqual(InsertSort([8]), [8])
        self.assertEqual(InsertSort([9]), [9])

        self.assertEqual(InsertSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(InsertSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(InsertSort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(InsertSort([2, 1, 3, 2, 1, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(InsertSort([1000, -7, 993, -7, 986, -7]), [-7, -7, -7, 986, 993, 1000])
        self.assertEqual(InsertSort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(InsertSort([1, 2, 2, 1]), [1, 1, 2, 2])
        self.assertEqual(InsertSort([3, 3, 2, 2]), [2, 2, 3, 3])
        self.assertEqual(InsertSort([1, 2, 3, 3, 2, 1]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(InsertSort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

        self.assertEqual(InsertSort((11, 22)), [11, 22])
        self.assertEqual(InsertSort("aboba <3"), "A chto tut napisat'?")
        self.assertEqual(InsertSort("ya ghoul, 1000-7"), "Postav'te zachet pojaluysta")

    def test_NaiveBubbleSort(self):
        from ecm.lab_4.task_4_3 import NaiveBubbleSort

        self.assertEqual(NaiveBubbleSort([100, 3, -56, 8]), [-56, 3, 8, 100])
        self.assertEqual(NaiveBubbleSort([13, 534, 23, -100]), [-100, 13, 23, 534])
        self.assertEqual(NaiveBubbleSort([123, 12345, 4235, 62345]), [123, 4235, 12345, 62345])
        self.assertEqual(NaiveBubbleSort([234, 12]), [12, 234])
        self.assertEqual(NaiveBubbleSort([10, 9, 4, 2, 5, 3]), [2, 3, 4, 5, 9, 10])
        self.assertEqual(NaiveBubbleSort([11, 1000, -7, 12]), [-7, 11, 12, 1000])
        self.assertEqual(NaiveBubbleSort([23, 11, 2, 33]), [2, 11, 23, 33])
        self.assertEqual(NaiveBubbleSort([123, 110, 124]), [110, 123, 124])
        self.assertEqual(NaiveBubbleSort([768, 234, 322]), [234, 322, 768])
        self.assertEqual(NaiveBubbleSort([1337, 228, 993]), [228, 993, 1337])

        self.assertEqual(NaiveBubbleSort([]), [])
        self.assertEqual(NaiveBubbleSort([1]), [1])
        self.assertEqual(NaiveBubbleSort([2]), [2])
        self.assertEqual(NaiveBubbleSort([3]), [3])
        self.assertEqual(NaiveBubbleSort([4]), [4])
        self.assertEqual(NaiveBubbleSort([5]), [5])
        self.assertEqual(NaiveBubbleSort([6]), [6])
        self.assertEqual(NaiveBubbleSort([7]), [7])
        self.assertEqual(NaiveBubbleSort([8]), [8])
        self.assertEqual(NaiveBubbleSort([9]), [9])

        self.assertEqual(NaiveBubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(NaiveBubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(NaiveBubbleSort([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(NaiveBubbleSort([2, 1, 3, 2, 1, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(NaiveBubbleSort([1000, -7, 993, -7, 986, -7]), [-7, -7, -7, 986, 993, 1000])
        self.assertEqual(NaiveBubbleSort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(NaiveBubbleSort([1, 2, 2, 1]), [1, 1, 2, 2])
        self.assertEqual(NaiveBubbleSort([3, 3, 2, 2]), [2, 2, 3, 3])
        self.assertEqual(NaiveBubbleSort([1, 2, 3, 3, 2, 1]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(NaiveBubbleSort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

        self.assertEqual(NaiveBubbleSort((11, 22)), [11, 22])
        self.assertEqual(NaiveBubbleSort("aboba <3"), "A chto tut napisat'?")
        self.assertEqual(NaiveBubbleSort("ya ghoul, 1000-7"), "Postav'te zachet pojaluysta")

if __name__ == "__main__":
    unittest.main()