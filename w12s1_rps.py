# This example will show case various ways to create a rock paper scissors program
# using functions from the random library
# More information here:
from random import *

# In this approach, we pick a random number between 1 and 3, then connect each number with a
# move in an if statement:
def taiwo_bot():
    x = randint(1, 3)
    if x == 1:
        return 'rock'
    elif x == 2:
        return 'paper'
    else:
        return 'scissors'

# In this approach, we put all the moves in a list, then we randomly generate an index
def nehemie_bot():
    moves = ['rock', 'paper', 'scissors']
    random_index = randint(0, len(moves) - 1)

    return moves[random_index]


# Note the choice method from the random library does the same as the above, just in 1 line.
def nadia_bot():
    moves = ['rock', 'paper', 'scissors']
    return choice(moves)

# Finally, we can use random to give each outcome a specific probability
# Below is an example of
def joyce_bot():
    x = random()
    if x < 0.5:
        return 'rock'
    elif x < 0.75:
        return 'paper'
    else:
        return 'scissors'

def rps_rules(move1, move2):
    if move1 == move2:
        print("It's a tie!")
    elif (move1 == 'rock' and move2 == 'paper') or \
            (move1 == 'paper' and move2 == 'scissors') or \
            (move1 == 'scissors' and move2 == 'rock'):
            print('Player 2 wins!')
    else:
        print('Player 1 wins!')

# rps_rules('paper', rps_bot())
rps_rules('rock',taiwo_bot())

# rps_rules('rock', 'rock')
# rps_rules('paper', 'paper')
# rps_rules('scissors', 'scissors')
# rps_rules('rock', 'scissors')
