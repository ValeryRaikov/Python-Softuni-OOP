from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0
        
    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        
        self.__manufacturer = value
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value: str):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        
        self.__model = value
        
    @property
    @abstractmethod
    def machine_type(self):
        pass
    
    @property
    @abstractmethod
    def processor_type(self):
        pass
    
    @property
    @abstractmethod
    def max_ram(self):
        pass
    
    @staticmethod
    def check_valid_ram(ram: int):
        result = log2(ram)
        return result.is_integer()
    
    def create_machine(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.processor_type[processor]
        self.price += int(log2(ram)) * 100
        
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processor_type:
            raise ValueError(f"{processor} is not compatible with {self.machine_type} {self.manufacturer} {self.model}!")
        
        if not self.check_valid_ram(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.machine_type} {self.manufacturer} {self.model}!")
        
        self.create_machine(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."
    
    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"