from project.user import User
from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 16) -> None:
        super().__init__(title, year, owner, age_restriction)
        
    @property
    def age_restriction(self):
        return self.__age_restriction
    
    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        
        self.__age_restriction = value
    
    def details(self) -> str:
        return f"Thriller - Title:{self.title}, Year:{self.year}," \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}," \
               f"Owned by:{self.owner.username}"