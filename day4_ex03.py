# Create a new tuple from the values you gathered using input. Make sure they're in the same
# order as the tuple you wrote in the movies list.

movies = [("Godzilla", "Gareth Edwards", "2014", "$160000000")]

title = input("Enter the movie title: ").strip().title()
director = input("Enter the director name: ").strip().title()
release_year = input("Enter the release year: ").strip()
budget = input("Enter the movie budget: ").strip()

new_movie = "title", "director", "release_year", "budget"
