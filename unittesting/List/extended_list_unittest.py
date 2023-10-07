from extended_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> object:
        self.integer_list = IntegerList(1, 2, 3, 4, 5)
        
    def test_integer_list_initialized_correctly(self):
        self.assertEqual(5, len(self.integer_list.get_data()))
        self.assertEqual(5, len(self.integer_list._IntegerList__data))
        
    def test_integer_list_get_data_correctly(self):
        self.assertEqual([1, 2, 3, 4, 5], self.integer_list.get_data())
        
    def test_integer_list_contains_non_integer_element(self):
        test_list = IntegerList(1, 2, 3.4)
        
        self.assertEqual(2, len(test_list.get_data()))
        self.assertEqual([1, 2], test_list.get_data())
        
    def test_add_method_not_int_error_raises(self):
        self.assertEqual(5, len(self.integer_list.get_data()))
        
        self.integer_list.add(6)
        
        self.assertEqual(6, len(self.integer_list.get_data()))
        
        TEST_DATA_VALUES = (7.8, "str", {}, [], None)
        
        for value in TEST_DATA_VALUES:
            with self.assertRaises(ValueError) as ex:
                self.integer_list.add(value)
            
        self.assertEqual("Element is not Integer", ex.exception.args[0])
        
    def test_add_method_adds_int(self):
        self.integer_list.add(6)
        
        self.assertEqual(6, len(self.integer_list.get_data()))
        self.assertEqual([1, 2, 3, 4, 5, 6], self.integer_list.get_data())
        self.assertIn(6, self.integer_list.get_data())
        
    def test_remove_method_invalid_index_error_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(9)
            
        self.assertEqual("Index is out of range", ex.exception.args[0]) 
        
    def test_remove_method_removes_index(self):
        self.assertEqual(5, len(self.integer_list.get_data()))
        
        self.integer_list.remove_index(1)
        
        self.assertEqual(4, len(self.integer_list.get_data()))
        self.assertNotIn(2, self.integer_list.get_data())
        self.assertEqual([1, 3, 4, 5], self.integer_list.get_data())
        
    def test_get_method_invalid_index_error_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(9)
            
        self.assertEqual("Index is out of range", ex.exception.args[0])
        
    def test_get_method_gets_index(self):
        self.assertEqual(5, len(self.integer_list.get_data()))
        
        self.assertEqual(4, self.integer_list.get(3))
        
    def test_insert_method_insert_index_error_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(9, 6)
            
        self.assertEqual("Index is out of range", ex.exception.args[0])
    
    def test_insert_method_element_not_int_error_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(0, "str")
            
        self.assertEqual("Element is not Integer", ex.exception.args[0])
        
    def test_insert_method_inserts_element_at_index(self):
        self.assertEqual(5, len(self.integer_list.get_data()))
        
        self.integer_list.insert(0, 6)
        
        self.assertEqual(6, len(self.integer_list.get_data()))
        self.assertIn(6, self.integer_list.get_data())
        self.assertEqual([6, 1, 2, 3, 4, 5], self.integer_list.get_data())
        
    def test_get_biggest_int(self):
        self.assertEqual(5, self.integer_list.get_biggest())
        
    def test_get_index(self):
        self.assertEqual(0, self.integer_list.get_index(1))
        
        
if __name__ == "__main__":
    unittest.main()