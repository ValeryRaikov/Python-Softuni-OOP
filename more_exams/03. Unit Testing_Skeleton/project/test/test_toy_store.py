from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()
    
    def test_toy_initialized_correctly(self):
        self.assertEqual(
            {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None,}, self.toy_store.toy_shelf
        )
        
    def test_add_toy_method_not_existing_shelf_raises(self):
        shelf = "X"
        toy_name = "Robot"
        
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy(shelf, toy_name)
        
        self.assertEqual("Shelf doesn't exist!", ex.exception.args[0])
        
    def test_add_method_toy_already_added_to_shelf_raises(self):
        shelf = "A"
        toy_name = "Robot"
        
        self.toy_store.toy_shelf[shelf] = toy_name
        
        self.assertEqual({"A": "Robot", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None,}, self.toy_store.toy_shelf)
        
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy(shelf, toy_name)
            
        self.assertEqual("Toy is already in shelf!", ex.exception.args[0])
        
    def test_add_method_shelf_already_full_raises(self):
        shelf = "A"
        toy_name = "Robot"
        
        self.toy_store.toy_shelf[shelf] = toy_name
        
        self.assertEqual({"A": "Robot", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None,}, self.toy_store.toy_shelf)
        
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy(shelf, toy_name = "Doll")
            
        self.assertEqual("Shelf is already taken!", ex.exception.args[0])
        
    def test_add_method_correct_execution(self):
        shelf = "A"
        toy_name = "Robot"
        
        result = self.toy_store.add_toy(shelf, toy_name)

        self.assertEqual({"A": "Robot", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None,}, self.toy_store.toy_shelf)
        self.assertEqual("Robot", self.toy_store.toy_shelf[shelf])
        self.assertEqual("Toy:Robot placed successfully!", result)
        
    def test_remove_toy_method_not_existing_shelf_raises(self):
        shelf = "X"
        toy_name = "Robot"
        
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy(shelf, toy_name)
        
        self.assertEqual("Shelf doesn't exist!", ex.exception.args[0])
        
    def test_remove_toy_method_toy_not_on_shelf_raises(self):
        shelf = "A"
        toy_name = "Robot"
        
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy(shelf, toy_name)
            
        self.assertEqual("Toy in that shelf doesn't exists!", ex.exception.args[0])
        
    def test_remove_toy_method_correct_execution(self):
        shelf = "A"
        toy_name = "Robot"
        
        self.toy_store.add_toy(shelf, toy_name)
        
        self.assertEqual("Robot", self.toy_store.toy_shelf[shelf])
        
        result = self.toy_store.remove_toy(shelf, toy_name)
        
        self.assertEqual(None, self.toy_store.toy_shelf[shelf])
        self.assertEqual("Remove toy:Robot successfully!", result)
        

if __name__ == "__main__":
    main()