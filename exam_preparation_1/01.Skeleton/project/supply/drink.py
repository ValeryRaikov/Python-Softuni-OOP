from project.supply.supply import Supply


class Drink(Supply):
    INITITAL_ENERGY = 15
    
    def __init__(self, name: str) -> None:
        super().__init__(name, Drink.INITITAL_ENERGY)
        
    def details(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"