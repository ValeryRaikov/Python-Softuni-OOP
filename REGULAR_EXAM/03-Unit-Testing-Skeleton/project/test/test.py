from project.second_hand_car import SecondHandCar

from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("E60", "passenger", 150000, 15000)
        
    def test_car_initialized_corrrectly(self):
        self.assertEqual("E60", self.car.model)
        self.assertEqual("passenger", self.car.car_type)
        self.assertEqual(150000, self.car.mileage)
        self.assertEqual(15000, self.car.price)
        self.assertEqual([], self.car.repairs)
        
    def test_price_property(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
            
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        
    def test_mileage_property(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 50
            
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))
        
    def test_set_promotional_price_raises(self):
        new_price = 18000
        
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(new_price)
            
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))
        
    def test_set_promotional_price_correct_implementation(self):
        new_price = 12000
        
        result = self.car.set_promotional_price(new_price)
        
        self.assertEqual(12000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)
        
    def test_need_repair_raises(self):
        repair_price = 10000
        repair_description = "Engine repair"
        
        result = self.car.need_repair(repair_price, repair_description)
        
        self.assertEqual('Repair is impossible!', result)
        
    def test_need_repair_correct_implementation(self):
        repair_price = 3000
        repair_description = "Engine repair"
        
        result = self.car.need_repair(repair_price, repair_description)
        
        self.assertEqual(18000, self.car.price)
        self.assertEqual(["Engine repair"], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)
        
    def test__gt__method_fail(self):
        other_car = SecondHandCar("S5", "coupe", 185000, 13000)
        
        result = self.car.__gt__(other_car)
        
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test__gt__method_success(self):
        other_car = SecondHandCar("A5", "passenger", 80000, 18000)
        
        result = self.car.__gt__(other_car)

        self.assertFalse(result)
    
    def test__str__method_correct_implementation(self):
        self.assertEqual(
            """Model E60 | Type passenger | Milage 150000km
Current price: 15000.00 | Number of Repairs: 0""", str(self.car)
        )
    

if __name__ == "__main__":
    main()