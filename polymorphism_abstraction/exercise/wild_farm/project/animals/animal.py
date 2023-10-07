from abc import ABC, abstractmethod
from typing import List
from project.food import Food


class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0
        
    @property
    @abstractmethod
    def food_that_is_eaten(self) -> List[Food]:
        pass
    
    @property
    @abstractmethod
    def gained_weight(self) -> float:
        pass
    
    @property
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    def feed(self, food: Food) -> None or str:
        if type(food) not in self.food_that_is_eaten:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.gained_weight
        self.food_eaten += food.quantity
        
        
class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
        
        
class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"