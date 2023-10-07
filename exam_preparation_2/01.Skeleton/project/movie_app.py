from project.movie_specification.movie import Movie
from project.user import User

from typing import List, Optional


class MovieApp:
    def __init__(self) -> None:
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []
        
    def check_existing_user(self, username: str) -> Optional[User]:
        try:
            existing_user = next(filter(lambda x: x.username == username, self.users_collection))
        except StopIteration:
            return
        
        return existing_user
    
    def check_existing_movie(self, movie: Movie) -> Optional[Movie]:
        try:
            existing_movie = next(filter(lambda x: x.title == movie.title, self.movies_collection))
        except StopIteration:
            return
        
        return existing_movie
    
    def check_is_movie_liked(self, username: str, movie: Movie) -> Optional[Movie]:
        existing_user = self.check_existing_user(username)
        
        try:
            liked_movie = next(filter(lambda x: x.title == movie.title, existing_user.movies_liked))
        except StopIteration:
            return
        
        return liked_movie
        
    def register_user(self, username: str, age: int) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        
        if existing_user:
            raise Exception("User already exists!")
        
        user = User(username, age)
        self.users_collection.append(user)
        
        return f"{username} registered successfully."
    
    def upload_movie(self, username: str, movie: Movie) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        
        if not existing_user:
            raise Exception("This user does not exist!")
        
        if movie.owner.username != existing_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        
        existing_movie = self.check_existing_movie(movie)
        
        if existing_movie:
            raise Exception("Movie already added to the collection!")
        
        self.movies_collection.append(movie)
        existing_user.movies_owned.append(movie)
        
        return f"{username} successfully added {movie.title} movie."
    
    def edit_movie(self, username: str, movie: Movie, **kwargs) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        existing_movie = self.check_existing_movie(movie)
        
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        
        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        
        for key, value in kwargs.items():
            setattr(movie, key, value)
            
        return f"{username} successfully edited {movie.title} movie."
        
    def delete_movie(self, username: str, movie: Movie) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        existing_movie = self.check_existing_movie(movie)
        
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        
        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        
        self.movies_collection.remove(movie)
        existing_user.movies_owned.remove(movie)
        
        return f"{username} successfully deleted {movie.title} movie."
    
    def like_movie(self, username: str, movie: Movie) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        
        if existing_user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        
        liked_movie = self.check_is_movie_liked(username, movie)
        
        if liked_movie:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        
        movie.likes += 1
        existing_user.movies_liked.append(movie)
        
        return f"{username} liked {movie.title} movie."
    
    def dislike_movie(self, username: str, movie: Movie) -> Optional[str]:
        existing_user = self.check_existing_user(username)
        
        if existing_user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        
        liked_movie = self.check_is_movie_liked(username, movie)
        
        if not liked_movie:
            return f"{username} has not liked the movie {movie.title}!"
        
        movie.likes -= 1
        existing_user.movies_liked.remove(movie)
        
        return f"{username} disliked {movie.title} movie."
    
    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."
        
        sorted_movies = sorted(self.movies_collection, key = lambda x: (-x.year, x.title))
        
        return "\n".join([x.details() for x in sorted_movies])
    
    def __str__(self) -> str:
        result = ""
        
        if not self.users_collection:
            result += "All users: No users.\n"
        
        if not self.movies_collection:
            result += "All movies: No movies.\n"
        
        result += f"All users: {', '.join([x.username for x in self.users_collection])}" + "\n"
        result += f"All movies: {', '.join(x.title for x in self.movies_collection)}" + "\n"
        
        return result
