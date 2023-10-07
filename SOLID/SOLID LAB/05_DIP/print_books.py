from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, content: str):
        self.content = content
        
    @abstractmethod
    def format(self, book) -> str:
        pass


class Formatter(Book):
    def format(self, book: Book) -> str:
        return book.content


class Printer(Formatter):
    def get_book(self, book: Book):
        formatted_book = book.format(book)
        return formatted_book