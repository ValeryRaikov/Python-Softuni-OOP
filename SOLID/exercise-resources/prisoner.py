class Person:
    def __init__(self, position) -> None:
        self.position = position


class FreePerson(Person):
    def walk_north(self, dist) -> None:
        self.position[1] += dist

    def walk_east(self, dist) -> None:
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self) -> None:
        super().__init__(self.PRISON_LOCATION)
        self.is_free = False



prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
