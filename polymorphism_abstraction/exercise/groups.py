from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other) -> object:
        new_person = Person(self.name, other.surname)

        return new_person


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other) -> object:
        new_group = Group(f"{self.name} {other.name}", self.people + other.people)

        return new_group

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(f'{p.name} {p.surname}' for p in self.people)}"

    def __getitem__(self, index: int) -> str:
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)
