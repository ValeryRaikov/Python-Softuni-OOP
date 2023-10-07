from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild = "Unaffiliated"
        
    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"
        
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"
    
    def player_info(self) -> str:
        skills_info = "\n".join([f"==={s_name} - {s_mana}" for s_name, s_mana in self.skills.items()])
        
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n" + \
               f"{skills_info}"