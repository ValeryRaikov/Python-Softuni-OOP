from typing import List

from project.animal import Animal
from project.worker import Worker
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []
        
    def add_animal(self, animal: Animal, price: int) -> str:
        is_budget_enough = self.__budget >= price
        is_capacity_enough = self.__animal_capacity > len(self.animals)
        
        if is_budget_enough and is_capacity_enough:
            self.animals.append(animal)
            self.__budget -= price
            
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif not is_budget_enough:
            return "Not enough budget"
        else:
            return "Not enough space for animal"
        
    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        
        self.workers.append(worker)
        
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    
    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = list(filter(lambda x: x.name == worker_name, self.workers))[0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"
        
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"
    
    def pay_workers(self) -> str:
        worker_salaries = sum([x.salary for x in self.workers])
        
        if self.__budget < worker_salaries:
            return "You have no budget to pay your workers. They are unhappy"
            
        self.__budget -= worker_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    
    def tend_animals(self) -> str:
        animals_expenses = sum([x.money_for_care for x in self.animals])
        
        if self.__budget < animals_expenses:
            return "You have no budget to tend the animals. They are unhappy."
        
        self.__budget -= animals_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    
    def profit(self, amount: int) -> None:
        self.__budget += amount
        
    def animals_status(self) -> str:
        lions = list(filter(lambda x: isinstance(x, Lion), self.animals))
        tigers = list(filter(lambda x: isinstance(x, Tiger), self.animals))
        cheetahs = list(filter(lambda x: isinstance(x, Cheetah), self.animals))
        
        output = f"You have {len(self.animals)} animals\n"
        output += f"----- {len(lions)} Lions:\n"
        output += ''.join([f'{x}\n' for x in lions])
        output += f"----- {len(tigers)} Tigers:\n"
        output += ''.join([f'{x}\n' for x in tigers])
        output += f"----- {len(cheetahs)} Cheetahs:\n"
        output += ''.join([f'{x}\n' for x in cheetahs])
               
        return output[:-1]
    
    def workers_status(self) -> str:
        keepers = list(filter(lambda x: isinstance(x, Keeper), self.workers))
        caretakers = list(filter(lambda x: isinstance(x, Caretaker), self.workers))
        vets = list(filter(lambda x: isinstance(x, Vet), self.workers))
        
        output = f"You have {len(self.workers)} workers\n"
        output += f"----- {len(keepers)} Keepers:\n"
        output += ''.join([f'{x}\n' for x in keepers])
        output += f"----- {len(caretakers)} Caretakers:\n"
        output += ''.join([f'{x}\n' for x in caretakers])
        output += f"----- {len(vets)} Vets:\n"
        output += ''.join([f'{x}\n' for x in vets])
               
        return output[:-1]