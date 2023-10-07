from typing import List, Tuple

from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = ["Food", "Drink"]
    
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.supplies: List[Supply] = []
        
    def add_player(self, *players: Tuple[Player]) -> str:
        players_names = []
        
        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_names.append(player.name)
                
        return f"Successfully added: {', '.join(players_names)}"
    
    def add_supply(self, *supplies: Tuple[Supply]) -> None:
        [self.supplies.append(supply) for supply in supplies]
        
    def sustain(self, player_name: str, sustenance_type: str) -> None or str:
        if sustenance_type not in Controller.VALID_TYPES:
            return
        
        for player in self.players:
            if player.name == player_name:
                break
        else:
            return
        
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        
        for i in range(len(self.supplies) - 1, -1 , -1):
            supply = self.supplies[i]
            
            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        
        player.stamina = min(100, player.stamina + supply.energy)
        
        return f"{player_name} sustained successfully with {supply.name}."
    
    def duel(self, first_player_name: str, second_player_name: str) -> None or str:
        players = [
            next(filter(lambda x: x.name == first_player_name, self.players)),
            next(filter(lambda x: x.name == second_player_name, self.players))
        ]
        
        sorted_players = sorted(players, key = lambda x: x.stamina)
        
        errors = []
        
        for player in sorted_players:
            if player.stamina <= 0:
                errors.append(f"Player {player.name} does not have enough stamina.")
                
        if errors:
            return "\n".join(errors)
        
        first_player_damage = sorted_players[0].stamina / 2
        sorted_players[1].stamina = max(sorted_players[1].stamina - first_player_damage, 0)
        
        second_player_damage = sorted_players[1].stamina / 2
        sorted_players[0].stamina = max(sorted_players[0].stamina - second_player_damage, 0)
        
        winner = sorted(sorted_players, key = lambda x: x.stamina, reverse = True)[0]
        
        return f"Winner: {winner.name}"
    
    def next_day(self) -> None:
         for player in self.players:
            reduce_stamina_ = player.age * 2
            player.stamina = max(player.stamina - reduce_stamina_, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")
            
    def __str__(self) -> str:
        result = [str(player) for player in self.players] + [supply.details() for supply in self.supplies]
        
        return "\n".join(result)
        