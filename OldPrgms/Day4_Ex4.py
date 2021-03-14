# 4) Use an f-string to print the movie name and release year by accessing your new movie tuple.

movies = [
	("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

title = input("Title: ")
director = input("Director: ")
year = input("Year of release: ")
budget = input("Budget: ")

new_movie = title, director, year, budget

print(f"{new_movie[0]} ({new_movie[2]})")