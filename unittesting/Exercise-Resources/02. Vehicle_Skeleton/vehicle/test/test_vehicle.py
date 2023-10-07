from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> object:
        self.vehicle = Vehicle(25.5, 220)
        
    def test_vehicle_default_fuel_consumption_attribute(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        
    def test_vehicle_initialized_correctly(self):
        self.assertEqual(25.5, self.vehicle.fuel)
        self.assertEqual(25.5, self.vehicle.capacity)
        self.assertEqual(220, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        
    def test_vehicle_drive_raises(self):
        test_kilometers = 100
        
        self.vehicle.fuel = 0
        
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(test_kilometers)
            
        self.assertEqual("Not enough fuel", str(ex.exception))
        
    def test_vehicle_drive_correct_fuel_decrease_expected(self):
        test_kilometers = 10
        expected_result = 25.5 - self.vehicle.fuel_consumption * test_kilometers
        
        self.vehicle.drive(test_kilometers)
        
        self.assertEqual(expected_result, self.vehicle.fuel)
        
    def test_vehicle_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
            
        self.assertEqual("Too much fuel", str(ex.exception))
        
    def test_vehicle_refuel_correct_fuel_increase_expected(self):
        self.vehicle.fuel = 10
        
        self.vehicle.refuel(10)
        
        self.assertEqual(20, self.vehicle.fuel)
        
    def test_vehicle__repr__method_return_correct_message(self):
        self.assertEqual("The vehicle has 220 " \
        "horse power with 25.5 fuel left and 1.25 fuel consumption", 
        str(self.vehicle))
        
        
if __name__ == "__main__":
    main()