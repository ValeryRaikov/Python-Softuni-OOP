from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
            
        self.pokemons.append(pokemon)
            
        return f"Caught {pokemon.pokemon_details()}"
    
    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
            
        return "Pokemon is not caught"
    
    def trainer_data(self) -> str:
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])
        
        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"
               
               
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())