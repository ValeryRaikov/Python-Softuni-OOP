from abc import ABC, abstractmethod
    

class BaseAnimal(ABC):
    def __init__(self, species):
        self.species = species
        
    def get_species(self):
        return self.species
    
    @staticmethod
    @abstractmethod
    def make_sound():
        pass
    
    
class Cat(BaseAnimal):
    def make_sound():
        return "meow meow"
    
class Dog(BaseAnimal):
    def make_sound():
        return "bark"


def animal_sound(animals: list):
        for animal in animals:
                print(animal.make_sound())

animals = [Cat('cat'), Dog('dog')]
#animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
