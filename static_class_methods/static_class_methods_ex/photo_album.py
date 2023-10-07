from typing import List

from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_pages(pages)
        self.idx = 0
        
    @staticmethod
    def __initialize_pages(pages) -> List[List[str]]:
        return [[] for _ in range(pages)]
    
    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)
    
    def add_photo(self, label:str) -> str:
        if len(self.photos[self.idx]) < PhotoAlbum.PHOTOS_PER_PAGE:
            self.photos[self.idx].append(label)
            return f"{label} photo added successfully on page {self.idx + 1} slot {self.photos[self.idx].index(label) + 1}"
        else:
            self.idx += 1
            
            if self.idx == len(self.photos):
                return "No more free slots"
            
            self.photos[self.idx].append(label)
            return f"{label} photo added successfully on page {self.idx + 1} slot {self.photos[self.idx].index(label) + 1}"
            
    def display(self) -> str:
        output = "-" * 11 + "\n"
        
        for page in self.photos:
            output += " ".join(["[]" for photo in page]) + "\n"
            output += "-" * 11 + "\n"
            
        return output
            
album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())