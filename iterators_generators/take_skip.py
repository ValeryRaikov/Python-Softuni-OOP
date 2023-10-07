class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current: int = -step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= (self.count - 1) * self.step:
            raise StopIteration

        self.current += self.step
        return self.current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
 print(number)