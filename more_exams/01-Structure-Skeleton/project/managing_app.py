from project.user import User
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan

from typing import List


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
    
    def __init__(self) -> None:
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []
      
    # helper methods  
    def check_is_user_existing(self, driving_license_number: str) -> User or None:
        try:
            user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        except IndexError:
            return
        
        if user:
            return user
        
    def check_is_vehicle_existing(self, license_plate_number: str) -> BaseVehicle or None:
        try:
            vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        except IndexError:
            return
        
        if vehicle:
            return vehicle
        
    def check_is_route_existing(self, start_point: str, end_point: str) -> Route or str:
        try:
            route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point][0]
        except IndexError:
            return
        
        if route:
            return route
        
    def find_route_by_id(self, route_id: int):
        try:
            route = [r for r in self.routes if r.route_id == route_id][0]
        except IndexError:
            return
        
        if route:
            return route
        
    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        existing_user = self.check_is_user_existing(driving_license_number)
        
        if existing_user:
            return f"{driving_license_number} has already been registered to our platform."
        
        current_user = User(first_name, last_name, driving_license_number)
        self.users.append(current_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
    
    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in ManagingApp.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        
        existing_vehicle = self.check_is_vehicle_existing(license_plate_number)
        
        if existing_vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        
        if vehicle_type == PassengerCar.__class__.__name__:
            current_vehicle = PassengerCar(brand, model, license_plate_number)
        else:
            current_vehicle = CargoVan(brand, model, license_plate_number)
        
        self.vehicles.append(current_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
    
    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        existing_route = self.check_is_route_existing(start_point, end_point)
        
        if existing_route:
            if existing_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            
            if existing_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            
            if existing_route.length > length:
                existing_route.is_locked = True
                
        current_route = Route(start_point, end_point, length, route_id = len(self.routes) + 1)
        self.routes.append(current_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
    
    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool) -> str:
        user = self.check_is_user_existing(driving_license_number)
        vehicle = self.check_is_vehicle_existing(license_plate_number)
        route = self.find_route_by_id(route_id)
        
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        
        vehicle.drive(route.length)
        
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
            
        return str(vehicle)
    
    def repair_vehicles(self, count: int) -> str:
        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key = lambda x: (x.brand, x.model))[: count]
        
        for vehicle in damaged_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        
        return f"{count} vehicles were successfully repaired!"
    
    def users_report(self) -> str:
        result = ["*** E-Drive-Rent ***", ]
        
        sorted_users = sorted(self.users, key = lambda x: -x.rating)
        
        result.append(('\n'.join(str(u) for u in sorted_users)))
        
        return '\n'.join(result)