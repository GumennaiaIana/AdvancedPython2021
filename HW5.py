# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:35:43 2021

@author: gunen
"""

class Movie:
    def __init__(self, name, director, year, country, duration, age_rating):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
    def is_allowed(self, other):
        if (2021 - other.year_of_birth) >= self.age_rating:
            return True
        else:
            return False

class Human:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth

class Cartoon(Movie):
    def __init__(self, name, director, year, country, duration, age_rating, technique):
        super().__init__(name, director, year, country, duration, age_rating)
        self.technique = technique

class Anime(Cartoon):
    def __init__(self, name, director, year, country, duration, age_rating, technique):
        super().__init__(name = name, director = director, year = year, country = 'Japan', duration = duration, age_rating = age_rating, technique = 'drawn')

movie = Movie(name = "Dune", director = "Denis Villeneuve", year = 2021, country = "USA", duration = 155, age_rating = 13)
human = Human(name = "Neo", sex = "M", year_of_birth = 1964)
print(movie.is_allowed(human))  