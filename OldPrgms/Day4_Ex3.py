# 3) Create a new tuple from the values you gathered using input. Make sure they're in the same order as the tuple you wrote in the movies

movies = [
	("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

title = input("Title: ")
director = input("Director: ")
year = input("Year of release: ")
budget = input("Budget: ")

new_movie = title, director, year, budget