from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    @abstractmethod
    def drive(self, distance) -> None:
        pass
    
    @abstractmethod
    def refuel(self, fuel) -> None:
        pass
    
    
class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9
    
    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + Car.AIR_CONDITIONER_CONSUMPTION) * distance
        
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption
    
    def refuel(self, fuel: int) -> None:
         self.fuel_quantity += fuel
         
    
class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    HOLE_IN_TANK = 0.95
    
    def drive(self, distance: int) -> None:  
        consumption = (self.fuel_consumption + Truck.AIR_CONDITIONER_CONSUMPTION) * distance
        
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption    
            
    def refuel(self, fuel: int) -> None:
         self.fuel_quantity += fuel * Truck.HOLE_IN_TANK
         
         
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)