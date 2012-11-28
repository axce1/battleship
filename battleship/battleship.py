##
# Lesson from Codecademy.com
##
# http://www.codecademy.com/ru/courses/python-beginner-en-4XuFm
##
# For python3
##

import random

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (*row, sep=" ")

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

turn = 0
for turn in range(4):
    print ("Turn: " + str(turn+1))

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    print (ship_row)
    print (ship_col)

    if guess_row == ship_row and \
        guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    elif turn == 3:
        print ("Game Over!")
    else:
        if (0 < guess_row and guess_row > 4) or (0 < guess_col and guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif (board[guess_row] [guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row] [guess_col] = "X"
    print_board(board)
    turn +=1
