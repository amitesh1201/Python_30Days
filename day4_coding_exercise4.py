"""
In this problem we have provided you with a set of lottery numbers:
You must define a list of two numbers, each with a name and another set of numbers.
"""

lottery_numbers = {13, 21, 22, 5, 8}

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        'name': 'Sam',
        'numbers': {13, 21, 44, 55, 10}
    },
    {
        'name': 'Ram',
        'numbers': {5, 15, 20, 25, 33}
    }
]


"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"{name} got {len(numbers)} number right.")


name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"{name} got {len(numbers)} number right.")
