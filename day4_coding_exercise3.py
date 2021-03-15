# Exercise : Nearby Friends
# We have provided you with tei variables

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friendname = input("Friend Name: ")

# Add the name to the empty set
user_friends.add(friendname)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

nearby_friends = nearby_people.intersection(user_friends)

print(nearby_friends)
