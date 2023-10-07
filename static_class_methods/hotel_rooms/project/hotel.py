from typing import List

from project.room import Room

class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0
        
    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")
    
    def add_room(self, room: Room) -> None:
        if room not in self.rooms:
            self.rooms.append(room)
            
    def take_room(self, room_number: int, people: int) -> None:
        try:
            room = [x for x in self.rooms if x.number == room_number][0]
        except IndexError:
            pass
        
        if not room.is_taken and room.capacity >= people:
            room.is_taken = True
            room.guests += people
            self.guests += people
            
    def free_room(self, room_number: int) -> None:
        try:
            room = [x for x in self.rooms if x.number == room_number][0]
        except IndexError:
            pass
        
        if room.is_taken:
            room.is_taken = False
            self.guests -= room.guests
            room.guests = 0
            
    def status(self) -> str:
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]
        
        return f"Hotel {self.name} has {self.guests} total guests\n" \
             + f"Free rooms: {', '.join(free_rooms)}\n" \
             + f"Taken rooms: {', '.join(taken_rooms)}"
            