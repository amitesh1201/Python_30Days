# 4. Format and print the information below using string interpolation:
# 
title = "Joker"
director = "Todd Phillips"
release_year = 2019
#
# The output should look like this:
# Joker (2019), directed by Todd Phillips

output = "{} ({}), directed by {}"
print(output.format("Joker", 2019, "Todd Phillips"))

output = "{title} ({release_year}), directed by {director}"
print(output.format(title="Joker", release_year=2019, director="Todd Phillips"))

print(f"{title} ({release_year}), directed by {director}")