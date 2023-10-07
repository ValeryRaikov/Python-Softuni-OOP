from car_manager import Car

import unittest

class CarTests(unittest.TestCase):
    def setUp(self) -> object:
        self.car = Car("Skoda", "Octavia", 6.5, 50)
    
    def test_car_initialized_correctly(self):
        self.assertEqual("Skoda", self.car.make)
        self.assertEqual("Octavia", self.car.model)
        self.assertEqual(6.5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)
        
    def test_car_make_property(self):
        expected_name = "Skoda"
        
        self.assertEqual(expected_name, self.car.make)
        self.assertEqual(expected_name, self.car._Car__make)
        
    def test_car_make_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
            
        self.assertEqual("Make cannot be null or empty!", ex.exception.args[0])
        
    def test_car_model_property(self):
        expected_name = "Octavia"
        
        self.assertEqual(expected_name, self.car.model)
        self.assertEqual(expected_name, self.car._Car__model)
        
    def test_car_model_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
            
        self.assertEqual("Model cannot be null or empty!", ex.exception.args[0])
        
    def test_car_fuel_consumption_property(self):
        expected_value = 6.5
        
        self.assertEqual(expected_value, self.car.fuel_consumption)
        self.assertEqual(expected_value, self.car._Car__fuel_consumption)
        
    def test_car_fuel_consumption_is_below_or_equal_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
            
        self.assertEqual("Fuel consumption cannot be zero or negative!", ex.exception.args[0])
        
    def test_car_fuel_capacity_property(self):
        expected_value = 50
        
        self.assertEqual(expected_value, self.car.fuel_capacity)
        self.assertEqual(expected_value, self.car._Car__fuel_capacity)
        
    def test_car_fuel_capacity_is_below_or_equal_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5
            
        self.assertEqual("Fuel capacity cannot be zero or negative!", ex.exception.args[0])
        
    def test_car_fuel_amount_property(self):
        expected_value = 0
        
        self.assertEqual(expected_value, self.car.fuel_amount)
        self.assertEqual(expected_value, self.car._Car__fuel_amount)
        
    def test_car_fuel_consumption_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
            
        self.assertEqual("Fuel amount cannot be negative!", ex.exception.args[0])
        
    def test_car_refuel_method_raises(self):
        fuel = 0
        
        with self.assertRaises(Exception) as ex:
            self.car.refuel(fuel)
            
        self.assertEqual("Fuel amount cannot be zero or negative!", ex.exception.args[0])
        
    def test_car_refuel_method_refuels_properly(self):
        fuel = 5
        expected_value = self.car.fuel_amount + fuel
        
        self.car.refuel(fuel)
            
        self.assertEqual(expected_value, self.car.fuel_amount)
        
    def test_car_fuel_amount_greater_than_fuel_capacity(self):
        self.car.fuel_amount = 45
        fuel = 7
        expected_value = self.car.fuel_capacity
        
        self.car.refuel(fuel)
        
        self.assertEqual(expected_value, self.car.fuel_amount)
        self.assertEqual(expected_value, self.car.fuel_capacity)
        
    def test_car_drive_method_raises(self):
        test_distance = 500
        
        with self.assertRaises(Exception) as ex:
            self.car.drive(test_distance)
            
        self.assertEqual("You don't have enough fuel to drive!", ex.exception.args[0])
        
    def test_car_drive_method_drives_properly(self):
        self.car.fuel_amount = 30
        distance = 300
        expected_value = self.car.fuel_amount - (distance / 100 * self.car.fuel_consumption)
        
        self.car.drive(distance)
        
        self.assertEqual(expected_value, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()