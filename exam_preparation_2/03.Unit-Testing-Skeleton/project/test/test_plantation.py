from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(100)
        
    def test_plantation_initialized_correctly(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)
        
    def test_size_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -5
            
        self.assertEqual("Size must be positive number!", str(ex.exception))
        
    def test_size_correct_set(self):
        self.plantation.size = 10
        self.assertEqual(10, self.plantation.size)
        
    def test_hire_worker_method_raises(self):
        worker = "Test Worker"
        
        self.plantation.hire_worker(worker)
        
        self.assertEqual(["Test Worker"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker(worker)
            
        self.assertEqual("Worker already hired!", str(ex.exception))
        
    def test_hire_worker_method_returns_proper_message(self):
        worker1 = "Test Worker"
        worker2 = "Test Worker2"
        
        result1 = self.plantation.hire_worker(worker1)
        self.plantation.hire_worker(worker2)
        
        self.assertEqual(["Test Worker", "Test Worker2"], self.plantation.workers)
        self.assertEqual(2, len(self.plantation.workers))
        self.assertEqual("Test Worker successfully hired.", result1)
        
    def test__len__method_empty_garden(self):
        garden_length = len(self.plantation.plants)
        
        self.assertEqual(0, garden_length)
        
    def test__len__method_non_empty_garden(self):
        self.plantation.plants = {"Test Worker": "tullip", "Test Worker2": "roses"}
        
        self.assertEqual("tullip", self.plantation.plants["Test Worker"])
        self.assertEqual("roses", self.plantation.plants["Test Worker2"])
        
        garden_length = len(self.plantation.plants)
        
        self.assertEqual(2, garden_length)
        
    def test_planting_method_raises(self):
        worker = "Test Worker"
        plant = "tullip"
        
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(worker, plant)
            
        self.assertEqual("Worker with name Test Worker is not hired!", str(ex.exception))
        
    def test_planting_method_plants_properly(self):
        worker = "Test Worker"
        plant = "tullip"
        
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        
        self.assertEqual(["tullip"], self.plantation.plants[worker])
        
    def test_planting_method_plantation_full_raises(self):
        self.plantation.size = 1
        worker = "Test Worker"
        worker2 = "test Worker2"
        plant = "tullip"
        plant2 = "daffodil"
        
        self.plantation.hire_worker(worker)
        self.plantation.hire_worker(worker2)
        
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting(worker, plant)
            self.plantation.planting(worker2, plant2)
        
        self.assertEqual("The plantation is full!", str(ex.exception))
        
    def test_is_worker_existing_in_plants_dict(self):
        self.assertEqual({}, self.plantation.plants)
        
        worker = "Test Worker"
        plant = "roses"
        
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        
        self.assertEqual(["roses"], self.plantation.plants[worker])
        
        self.plantation.planting(worker, "daffodil")
        
        self.assertEqual(["roses", "daffodil"], self.plantation.plants[worker])
        
    def test_plantation_method_return_message(self):
        self.plantation.hire_worker("Test Worker")
        
        self.plantation.plants = {"Test Worker": []}
        result = self.plantation.planting("Test Worker", "tullip")
        
        self.assertEqual("Test Worker planted tullip.", result)
        
    def test_plantation_worker_not_in_plants_dict(self):
        self.assertEqual({}, self.plantation.plants)
        
        self.plantation.hire_worker("Test Worker")
        result = self.plantation.planting("Test Worker", "tullip")
        
        self.assertEqual(["tullip"], self.plantation.plants["Test Worker"])
        self.assertEqual("Test Worker planted it's first tullip.", result)
        
    def test__str__method_returns_correct(self):
        worker = "Test Worker"
        worker2 = "Test Worker2"
        plant = "tullip"
        plant2 = "daffodil"
        
        self.plantation.hire_worker(worker)
        self.plantation.hire_worker(worker2)
        
        self.plantation.planting(worker, plant)
        self.plantation.planting(worker2, plant2)
        
        result = str(self.plantation)
        expected = "Plantation size: 100\nTest Worker, Test Worker2\nTest Worker planted: tullip\nTest Worker2 planted: daffodil"
        
        self.assertEqual(expected, result)
        
    def test__repr__method_returns_correct(self):
        worker = "Test Worker"
        worker2 = "Test Worker2"
        
        self.plantation.hire_worker(worker)
        self.plantation.hire_worker(worker2)
        
        result = repr(self.plantation)
        expected = "Size: 100\nWorkers: Test Worker, Test Worker2"
        
        self.assertEqual(expected, result)
        
        
if __name__ == "__main__":
    main()