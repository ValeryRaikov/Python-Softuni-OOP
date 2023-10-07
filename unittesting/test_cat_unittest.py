from test_cat import Cat

import unittest

class CatTests(unittest.TestCase):
    def setUp(self) -> object:
        self.cat = Cat("Candy")
        
    def test_cat_initialized_correctly(self):
        self.assertEqual("Candy", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
        
    def test_cat_already_fed(self):
        self.cat.fed = True
        
        self.assertTrue(self.cat.fed)
        
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
            
        self.assertEqual('Already fed.', ex.exception.args[0])
        
        self.cat.fed = False
        
        self.assertFalse(self.cat.fed)
        
        # logic described down...
        
    def test_cat_atrributes_set_correctly_after_eat(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
        
        self.cat.eat()
        
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)
        
    def test_cat_cannot_fall_asleep(self):
        self.assertFalse(self.cat.fed)
        
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
            
        self.assertEqual('Cannot sleep while hungry', ex.exception.args[0])
        
        self.cat.fed = True
        
        self.assertTrue(self.cat.fed)
        
        self.cat.sleep()
        
        self.assertFalse(self.cat.sleepy)
        
    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.eat()
        
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        
        self.cat.sleep()
        
        self.assertFalse(self.cat.sleepy)
        
        
if __name__== "__main__":
    unittest.main()