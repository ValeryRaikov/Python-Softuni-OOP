from typing import List


class Book:
    def __init__(self, title: str, author: str, pages: int = 250) -> None:
        self.title = title
        self.author = author
        self.pages: int = pages
        
    def turn_page(self, page: int) -> str:
        if page > self.pages:
            return f"Page {page} does not exist!"
        
        self.page = page
        return f"Current page: {self.page}"
    
    def __repr__(self) -> str:
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}"
        
class Library:
    def __init__(self, books: List[Book], location: str) -> None:
        self.books = books
        self.location = location

    def find_book(self, title: str) -> Book:
        try:
            book = next(filter(lambda x: x.title == title, self.books))
        except StopIteration:
            return f"No book with title '{title}' found!"
        
        return book
    
b1 = Book("ABC", "J.K.R", 180)
b2 = Book("Test", "Testov")
b3 = Book("Python_tutorial", "Valery", 150)
b4 = Book("FFF", "Testov2")

print(b1.turn_page(10))
print(b2.turn_page(255))

l1 = Library([b1, b2, b3, b4], "Sofia - Mladost4")

print(l1.find_book("Python_tutorial"))