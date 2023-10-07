class dictionary_iter:
    def __init__(self, dict: dict) -> None:
       self.items = list(dict.items())
       self.index = -1
       
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.items):
            raise StopIteration
        
        return self.items[self.index]
    
    
"""class dictionary_iter:
    def __init__(self, dict: dict) -> None:
       self.items = list(dict.items())
       
    def __iter__(self):
        return iter(self.items)"""


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
 
result = dictionary_iter({"name": "Peter", 
"age": 24})
for x in result:
    print(x)