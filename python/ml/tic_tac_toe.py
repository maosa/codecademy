def print_board(board):
    print("|-------------|")
    print("| Tic Tac Toe |")
    print("|-------------|")
    print("|             |")
    print("|    " + board[0][0] + " " + board[0][1] + " " + board[0][2] + "    |")
    print("|    " + board[1][0] + " " + board[1][1] + " " + board[1][2] + "    |")
    print("|    " + board[2][0] + " " + board[2][1] + " " + board[2][2] + "    |")
    print("|             |")
    print("|-------------|")
    print()


def select_space(board, move, turn):
    if move not in range(1,10):
        return False
    row = int((move-1)/3)
    col = (move-1)%3
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        return False

def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves

def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
