from test_worker import Worker

import unittest

    
class WorkerTests(unittest.TestCase):
    def setUp(self) -> object:
        self.worker = Worker("Test", 2000, 50)
    
    def test_worker_initialized_correctly(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)
        
    def test_worker_has_enough_energy_to_work(self):
        worker = Worker("Test", 2000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
            
        self.assertEqual('Not enough energy.', ex.exception.args[0])
        
    def test_worker_can_work(self):
        self.assertEqual(0, self.worker.money)
        self.assertEqual(50, self.worker.energy)
        
        self.worker.work()
        
        self.assertEqual(2000, self.worker.money)
        self.assertEqual(49, self.worker.energy)
        
        self.worker.work()
        
        self.assertEqual(4000, self.worker.money)
        self.assertEqual(48, self.worker.energy)
        
    def test_worker_rest(self):
        self.worker.rest()
        
        self.assertEqual(51, self.worker.energy)
        
    def test_worker_get_info(self):    
        self.assertEqual("Test has saved 0 money.", self.worker.get_info())
        
        self.worker.work()
        
        self.assertEqual("Test has saved 2000 money.", self.worker.get_info())
                
        
if __name__ == "__main__":
    unittest.main()