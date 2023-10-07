from typing import List


class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []
        
    def __str__(self) -> str:
        return f"[{', '.join(reversed(self.data))}]"
        
    def push(self, element: str) -> None:
        self.data.append(element)
        
    def pop(self) -> str:
        if self.data:
            return self.data.pop()
        
    def top(self) -> str:
        if self.data:
            return self.data[-1]
        
    def is_empty(self) -> bool:
        is_empty = False if self.data else True
        
        return is_empty
    

s = Stack()
print(s)
s.push('a')
s.push('b')
s.pop()
print(s)
print(s.top())
print(s.is_empty())