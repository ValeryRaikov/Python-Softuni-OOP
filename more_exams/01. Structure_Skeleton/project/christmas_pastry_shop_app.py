from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen

from typing import List


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
    
    def __init__(self) -> None:
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0
        
    #helper methods
    def check_for_delicacy_existance(self, name: str) -> Delicacy or None:
        try:
            delicacy = [d for d in self.delicacies if d.name == name][0]
        except IndexError:
            return
        
        return delicacy
    
    def check_for_booth_existance(self, booth_number: int) -> Booth or None:
        try:
            booth = [b for b in self.booths if b.booth_number == booth_number][0]
        except IndexError:
            return
        
        return booth
        
    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        existing_delicacy = self.check_for_delicacy_existance(name)
        
        if existing_delicacy is not None:
            raise Exception(f"{name} already exists!")
        
        if type_delicacy not in ChristmasPastryShopApp.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        
        delicacy = ChristmasPastryShopApp.DELICACY_TYPES[type_delicacy](name, price)
        
        self.delicacies.append(delicacy)
        
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
    
    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        existing_booth = self.check_for_booth_existance(booth_number)
        
        if existing_booth is not None:
            raise Exception(f"Booth number {booth_number} already exists!")
        
        if type_booth not in ChristmasPastryShopApp.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        
        booth = ChristmasPastryShopApp.BOOTH_TYPES[type_booth](booth_number, capacity)
        
        self.booths.append(booth)
        
        return f"Added booth number {booth_number} in the pastry shop."
    
    def reserve_booth(self, number_of_people: int) -> str:
        try:
            wanted_booth = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people][0]
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")
        
        wanted_booth.is_reserved = True
        wanted_booth.reserve(number_of_people)
        
        return f"Booth {wanted_booth.booth_number} has been reserved for {number_of_people} people."
    
    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        wanted_booth = self.check_for_booth_existance(booth_number)
        wanted_delicay = self.check_for_delicacy_existance(delicacy_name)
        
        if wanted_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        
        if wanted_delicay is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        
        wanted_booth.delicacy_orders.append(wanted_delicay)
        
        return f"Booth {booth_number} ordered {delicacy_name}."
    
    def leave_booth(self, booth_number: int) -> str:
        wanted_booth = self.check_for_booth_existance(booth_number)
        bill = wanted_booth.price_for_reservation + sum(d.price for d in wanted_booth.delicacy_orders)
        wanted_booth.delicacy_orders = []
        wanted_booth.price_for_reservation = 0
        wanted_booth.is_reserved = False
        self.income += bill
        
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."    
    
    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."