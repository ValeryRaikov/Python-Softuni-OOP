from typing import List

from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []
      
    @staticmethod 
    def dvd_capacity() -> int:
        return 15
    
    @staticmethod
    def customer_capacity() -> int:
        return 10
    
    def add_customer(self, customer: Customer) -> None:
        if MovieWorld.customer_capacity() > len(self.customers):
            if customer not in self.customers:
                self.customers.append(customer)
            
    def add_dvd(self, dvd: DVD) -> None:
        if MovieWorld.dvd_capacity() > len(self.dvds):
            if dvd not in self.dvds:
                self.dvds.append(dvd)
            
    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        try:
            customer = next(filter(lambda x: x.id == customer_id, self.customers))
            dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            pass
        
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        
        if dvd.is_rented:
            return "DVD is already rented"
        
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        
        return f"{customer.name} has successfully rented {dvd.name}"
    
    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        try:
            customer = next(filter(lambda x: x.id == customer_id, self.customers))
            dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            pass
        
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        
        return f"{customer.name} has successfully returned {dvd.name}"
    
    def __repr__(self) -> str:
        customer_info = "\n".join([f"{x}" for x in self.customers])
        dvd_info = "\n".join([f"{x}" for x in self.dvds])
        
        return f"{customer_info}\n{dvd_info}"