from typing import Sequence


class sequence_repeat:
    def __init__(self, sequence: Sequence, number: int) -> None:
        self.sequnce = sequence
        self.number = number
        self.start: int = -1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.start += 1
        if self.start >= self.number:
            raise StopIteration
        
        return self.sequnce[self.start % len(self.sequnce)]
    

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
    
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')