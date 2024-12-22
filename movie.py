import json
from pathlib import Path
import logging

BASE_DIR = Path.cwd() / "data"
FILE_DIR = BASE_DIR / "movies.json"

def get_movies():
    with open(FILE_DIR, "r") as f:
        movie_list = json.load(f)   
    movies = [Movie(i) for i in movie_list]
    return movies
           
class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return f"{self.title}"
    
    def _get_movies(self):
        with open(FILE_DIR, "r") as f:
            movies = json.load(f)
        return movies

    def _write_movies(self, movies):
        with open(FILE_DIR, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()
        if not self.title in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} est déjà dans la liste !")
            return False
        
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} n'est pas dans la liste !")
            return False
        
#if __name__ == "__main__":
#    m = Movie("Genereau")
#    m.remove_from_movies()

movies = get_movies()
print(movies)