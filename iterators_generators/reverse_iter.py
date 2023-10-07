from typing import Sequence


class reverse_iter:
    def __init__(self, collection: Sequence) -> None:
        self.collection = collection
        self.start: int = len(self.collection)
        self.end: int = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.start -= 1
        if self.start < self.end:
            raise StopIteration
        
        return self.collection[self.start]


"""class reverse_iter:
    def __init__(self, collection: Sequence) -> None:
        self.collection = collection
        
    def __iter__(self):
        return reversed(self.collection)"""
    
        
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
 print(item)