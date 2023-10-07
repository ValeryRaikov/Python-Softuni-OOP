from abc import ABC, abstractmethod
from typing import List


class Vehicle(ABC):
    def __init__(self, brand, model, engine, horse_power) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine
        self.horse_power = horse_power
        self.fuel_type = None

    @abstractmethod
    def details(self) -> str:
        pass


class DieselCar(Vehicle):
    def __init__(self, brand, model, engine, horse_power, fuel_type="diesel") -> None:
        super().__init__(brand, model, engine, horse_power)
        self.fuel_type = fuel_type

    def details(self) -> str:
        return f"Car: {self.brand} {self.model} with {self.engine} engine, running on {self.fuel_type}, " \
               f"putting out {self.horse_power}"


class PetrolCar(Vehicle):
    def __init__(self, brand, model, engine, horse_power, fuel_type="petrol") -> None:
        super().__init__(brand, model, engine, horse_power)
        self.fuel_type = fuel_type

    def details(self) -> str:
        return f"Car: {self.brand} {self.model} with {self.engine} engine, running on {self.fuel_type}, " \
               f"putting out {self.horse_power}"


class ElectricCar(Vehicle):
    def __init__(self, brand, model, engine, horse_power, fuel_type="electricity") -> None:
        super().__init__(brand, model, engine, horse_power)
        self.fuel_type = fuel_type

    def details(self) -> str:
        return f"Car: {self.brand} {self.model} with {self.engine} engine, running on {self.fuel_type}, " \
               f"putting out {self.horse_power}"


class VehicleApp:
    AVAILABLE_VEHICLES = {
        "DieselCar": DieselCar, "PetrolCar": PetrolCar, "ElectricCar": ElectricCar
    }

    def __init__(self) -> None:
        self.diesel_cars: List[DieselCar] = []
        self.petrol_cars: List[PetrolCar] = []
        self.electric_cars: List[ElectricCar] = []
        self.vehicles = []

    def configure_vehicle(self, vehicle_type: str, brand: str, model: str, engine: str, horse_power: int) -> str:
        if vehicle_type not in VehicleApp.AVAILABLE_VEHICLES.keys():
            return f"{vehicle_type} is not supported by our app."

        try:
            vehicle_to_append = next(filter(lambda x: (x.brand == brand and x.model == model), self.vehicles))
        except StopIteration:
            return f"Sorry, {vehicle_type} out of stock!"

        vehicle_to_append = VehicleApp.AVAILABLE_VEHICLES[vehicle_type](brand, model, engine, horse_power)
        
        self.vehicles.remove(vehicle_to_append)

        if isinstance(vehicle_to_append, DieselCar):
            self.diesel_cars.remove(vehicle_to_append)
        elif isinstance(vehicle_to_append, PetrolCar):
            self.petrol_cars.remove(vehicle_to_append)
        elif isinstance(vehicle_to_append, ElectricCar):
            self.electric_cars.remove(vehicle_to_append)

        return f"Successfully found vehicle of {vehicle_type}: {vehicle_to_append.details()}"


car1 = DieselCar("Skoda", "Octavia", "diesel inner combustion", 150)
car2 = PetrolCar("Peugeot", "508", "petrol inner combustion", 180)
car3 = ElectricCar("Tesla", "Model Y", "electric", 450)

print(car1.details())
print(car2.details())
print(car3.details())

vehicle = VehicleApp()
vehicle.vehicles.append(car1)
vehicle.diesel_cars.append(car1)

print(vehicle.configure_vehicle("DieselCar", "Skoda", "Octavia", "diesel inner combustion", 150))