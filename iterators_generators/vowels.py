class vowels:
    VOWELS = ['a', 'o', 'u', 'e', 'i', 'y']
    
    def __init__(self, text: str) -> None:
        self.text = text
        self.curr_idx: int = -1
        self.end: int = len(self.text) - 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.curr_idx += 1
        if self.curr_idx > self.end:
            raise StopIteration
        
        if self.text[self.curr_idx].lower() in vowels.VOWELS:
            return self.text[self.curr_idx]
        
        return self.__next__()
        
        
my_string = vowels('Abcedifuty0o')
for char in my_string:
 print(char)