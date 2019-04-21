from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Hide the ship's coordinates
#print(ship_row)
#print(ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
    print("\nTurn", turn + 1)
    guess_row = int(input("Guess row: "))
    guess_col = int(input("Guess column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("\nCongratulations! You sank my battleship!\n")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("\nOops, that's not even in the ocean.\n")
        elif board[guess_row][guess_col] == "X":
            print("\nYou guessed that one already.\n")
        else:
            print("\nYou missed my battleship!\n")
            board[guess_row][guess_col] = "X"
        print_board(board)

    if turn == 3:
        print("\nShip's coordinates are: (", ship_row, ",", ship_col, ")")
        print("\nGAME OVER...\n")
