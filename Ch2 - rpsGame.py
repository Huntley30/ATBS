# Flow Control

import random
import sys

print('Rock, Paper, Scissors')

# These variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

while True:  # the main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissor or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # break out of the player input loop.
        print('Type one of r, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('Player Choice: ROCK versus...')
    elif playerMove == 'p':
        print('Player Choice: PAPER versus...')
    elif playerMove == 's':
        print('Player Choice: SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Computer Choice: ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Computer Choice: PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('Computer Choice: SCISSORS')

    # Display and record the wins/loss/tie:
    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':  # rock beats scissors
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':  # paper beats rock
        print('You Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':  # scissors beats paper
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':  # rock loses to paper
        print('You Lose :(!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':  # paper loses to scissors
        print('You Lose :(!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':  # scissors loses to rock
        print('You Lose :(!')
        losses = losses + 1
