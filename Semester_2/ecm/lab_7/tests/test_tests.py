import unittest
import init_test
from Semester_2.ecm.lab_7.task_7_7 import *

class TestTask_7_6_and_7_7(unittest.TestCase):
    def setUp(self):
        self.linked_list = MyList()
        self.linked_list.append('Data 1')
        self.linked_list.append('Data 2')
        
    def test_init_1(self):
        self.test_linked_list = MyList()
        self.assertTrue(self.test_linked_list.get_head() == self.test_linked_list.get_tail())
        
    def test_init_2(self):
        self.test_linked_list_2 = MyList()
        self.assertTrue(self.test_linked_list_2.get_tail().get_next() == self.test_linked_list_2.get_tail().get_prev())
    
    def test_append_1(self):
        self.assertTrue(self.linked_list.get_tail().get_data() == 'Data 2')
        
    def test_append_2(self):
        self.assertIsNone(self.linked_list.get_tail().get_next())
        
    def test_append_3(self):
        self.assertTrue(self.linked_list.get_head().get_next() == self.linked_list.get_tail().get_prev())

    def test_append_4(self):
        self.assertTrue(self.linked_list.get_head().get_next().get_prev() == self.linked_list.get_head())
        
    def test_append_5(self):
        self.linked_list.append('Data 3')
        self.assertTrue(self.linked_list.get_tail().get_data() == 'Data 3')
        
    def test_pop_1(self):
        self.assertEqual(self.linked_list.pop(), 'Data 2')
        
    def test_pop_2(self):
        self.linked_list.pop()
        self.assertTrue(self.linked_list.get_tail() == self.linked_list.get_head().get_next())

    def test_pop_3(self):
        self.linked_list.pop()
        self.linked_list.pop()
        self.assertRaises(EmptyLinkedList, self.linked_list.pop)
        
    def test_push_first_1(self):
        self.linked_list.push_first('Data Push')
        self.assertTrue('Data Push' == self.linked_list.get_head().get_next().get_data())
        
    def test_push_first_2(self):
        test_item = self.linked_list.get_head().get_next()
        self.linked_list.push_first('Data Push')
        self.assertTrue(self.linked_list.get_head().get_next().get_next() == test_item)
        
    def test_pop_fisrt_1(self):
        self.assertTrue(self.linked_list.pop_first() == 'Data 1')
        
    def test_pop_first_2(self):
        test_item = self.linked_list.get_tail()
        self.linked_list.pop_first()
        self.assertTrue(self.linked_list.get_head().get_next() == test_item)
    
    def test_pop_first_3(self):
        self.linked_list.pop_first()
        self.linked_list.pop_first()
        self.assertRaises(EmptyLinkedList, self.linked_list.pop_first)
        
    def test_len(self):
        self.assertEqual(len(self.linked_list), 2)
        
    def test_str(self):
        self.assertEqual(str(self.linked_list), "['Data 1', 'Data 2']")
        
    def test_add_after_1(self):
        self.linked_list.add_after(self.linked_list.find('Data 1'), 'Data Add After')
        self.assertEqual(str(self.linked_list), "[Data 1, Data Add After, Data 2]")
        
    def test_add_after_2(self):
        args = [None, 'Data Add After']
        self.assertRaises(Exception, self.linked_list.add_after, *args)
        
    def test_remove_1(self):
        self.linked_list.remove(self.linked_list.find('Data 2'))
        self.assertTrue(self.linked_list.get_head().get_next() == self.linked_list.get_tail())
        
    def test_remove_2(self):
        self.linked_list.remove(self.linked_list.find('Data 1'))
        self.assertTrue(self.linked_list.get_head().get_next()
                        == self.linked_list.get_tail())
        
    def test_remove_3(self):
        self.linked_list.remove(self.linked_list.find('Data 1'))
        self.linked_list.remove(self.linked_list.find('Data 2'))
        self.assertTrue(self.linked_list.get_head().get_next()
                        == self.linked_list.get_tail().get_prev())
        
    def test_remove_4(self):
        args = [self.linked_list.get_head()]
        self.assertRaises(Exception, self.linked_list.remove, *args)
        
    def test_remove_5(self):
        args = [self.linked_list.find(3)]
        self.assertRaises(Exception, self.linked_list.remove, *args)
        
    def test_find_1(self):
        self.assertTrue(self.linked_list.find('Data 1') == self.linked_list.get_head().get_next())
        
    def test_getitem_1(self):
        self.assertEqual(self.linked_list[0], 'Data 1')
        
    def test_getitem_2(self):
        self.assertEqual(self.linked_list[1], 'Data 2')

    def test_getitem_3(self):
        args = [2]
        self.assertRaises(IndexError, self.linked_list.__getitem__, *args)
        
    def test_getitem_4(self):
        args = [-1]
        self.assertRaises(IndexError, self.linked_list.__getitem__, *args)

    def test_setitem_1(self):
        self.linked_list[1] = 'Data 2 New'
        self.assertEqual(self.linked_list[1], 'Data 2 New')

    def test_setitem_2(self):
        self.linked_list[1] = 'Data 2 New'
        self.assertEqual(self.linked_list[1], 'Data 2 New')
        
    def test_setitem_3(self):
        args = [2, 'Data']
        self.assertRaises(IndexError, self.linked_list.__setitem__, *args)

    def test_setitem_4(self):
        args = [-1, 'Data']
        self.assertRaises(IndexError, self.linked_list.__setitem__, *args)
        
    def test_contains_1(self):
        self.assertFalse('Data' in self.linked_list)
    
    def test_contains_2(self):
        self.assertTrue('Data 1' in self.linked_list)
        
    # def test_add_1(self):
    #     temp_list = MyList()
    #     linked_list = self.linked_list + temp_list
    #     self.assertEqual(str(linked_list), "['Data 1', 'Data 2']")
        
    # def test_add_2(self):
    #     temp_list = MyList()
    #     temp_list.append('Data 3')
    #     linked_list = self.linked_list + temp_list
    #     self.assertEqual(str(linked_list), "['Data 1', 'Data 2', 'Data 3']")
        
    def test_concat_1(self):
        temp_list = MyList()
        temp_list.append('Data 3')
        self.linked_list.concat(temp_list)
        self.assertEqual(str(self.linked_list), "['Data 1', 'Data 2', 'Data 3']")
        self.assertEqual(str(temp_list),'[]')
        
    def test_concat_2(self):
        temp_list = MyList()
        temp_list.append('Data 3')
        temp_list.concat(self.linked_list)
        self.assertEqual(str(temp_list), "['Data 3', 'Data 1', 'Data 2']")
        self.assertEqual(str(self.linked_list), '[]')
    
    def test_iter_1(self):
        test_result = []
        for data in self.linked_list:
            test_result.append(data)
        self.assertTrue(str(test_result) == str(self.linked_list))
        
test_lab_7_suite = unittest.TestSuite()

test_lab_7_suite.addTest(unittest.makeSuite(TestTask_7_6_and_7_7))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_lab_7_suite)
    print(f'Errors: {len(result.errors)}')
    print(f'Failures: {len(result.failures)}')
    print(f'Skipped: {len(result.skipped)}')