from project.robot import Robot

from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("abc", "Education", 10, 2999.99)
        self.other_robot = Robot("def", "Military", 50, 9999.99)
        
    def test_robot_itialized_correctly(self):
        self.assertEqual("abc", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(2999.99, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
        
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)
        
    def test_category_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Civil"
            
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ex.exception))
        
    def test_price_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -10
            
        self.assertEqual("Price cannot be negative!", str(ex.exception))
        
    def test_upgrade_method_existing_hardware_component(self):
        hardware_component = "hard disk"
        component_price = 400.00
        
        self.robot.hardware_upgrades.append(hardware_component)
        
        result = self.robot.upgrade(hardware_component, component_price)
        
        self.assertEqual("Robot abc was not upgraded.", result)
        
    def test_upgrade_method_not_existing_hardware_component(self):
        hardware_component = "hard disk"
        component_price = 400.00
        
        result = self.robot.upgrade(hardware_component, component_price)
        
        self.assertEqual(["hard disk"], self.robot.hardware_upgrades)
        self.assertEqual(3599.99, self.robot.price)
        self.assertEqual("Robot abc was upgraded with hard disk.", result)
        
    def test_update_method_existing_software_component_version_fail(self):
        self.robot.software_updates.append(8.0)
        
        version = 7.8
        needed_capacity = 4
        
        result = self.robot.update(version, needed_capacity)
        
        self.assertEqual("Robot abc was not updated.", result)
        
    def test_update_method_existing_software_component_capacity_fail(self):
        self.robot.software_updates.append(7.7)
        
        version = 7.8
        needed_capacity = 12
        
        result = self.robot.update(version, needed_capacity)
        
        self.assertEqual("Robot abc was not updated.", result)
        
    def test_update_method_existing_software_success(self):
        self.robot.software_updates.append(7.7)
        
        version = 7.8
        needed_capacity = 4
        
        result = self.robot.update(version, needed_capacity)
        
        self.assertEqual([7.7, 7.8], self.robot.software_updates)
        self.assertEqual(6, self.robot.available_capacity)
        self.assertEqual("Robot abc was updated to version 7.8.", result)
        
    def test__gt__method_greater(self):
        result = self.other_robot.__gt__(self.robot)
        
        self.assertEqual("Robot with ID def is more expensive than Robot with ID abc.", result)
        
    def test__gt__method_equal(self):
        self.other_robot.price = 2999.99
        
        result = self.robot.__gt__(self.other_robot)
        
        self.assertEqual("Robot with ID abc costs equal to Robot with ID def.", result)
        
    def test__gt__method_cheaper(self):
        result = self.robot.__gt__(self.other_robot)
        
        self.assertEqual("Robot with ID abc is cheaper than Robot with ID def.", result)
        

if __name__ == "__main__":
    main()