class User:
    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        
        self.__username = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        
        self.__age = value
    
    def __str__(self) -> str:
        result = f"Username: {self.username}, Age: {self.age}\n"
        
        result += "Liked movies:\n"
        
        if not self.movies_liked:
            result += "No movies liked."
        else:
            result += "\n".join([x.details() for x in self.movies_liked]) + "\n"
            
        result += "Owned movies:\n"
               
        if not self.movies_owned:
            result += "No movies owned.\n"
        else:
            result += "\n".join([x.details() for x in self.movies_owned])
    
        return result