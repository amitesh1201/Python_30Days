# Print both movies in the movies collection.

movies = [("Godzilla", "Gareth Edwards", "2014", "$160000000")]

title = input("Enter the movie title: ").strip().title()
director = input("Enter the director name: ").strip().title()
release_year = input("Enter the release year: ").strip()
budget = input("Enter the movie budget: ").strip()

new_movie = (title, director, release_year, budget)

print(f"{new_movie[0]} ({new_movie[2]})")

movies.append(new_movie)

print(movies[0])
print(movies[1])
