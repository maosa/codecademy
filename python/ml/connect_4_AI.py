##### CONNECT FOUR - MINIMAX PROJECT

from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      ##### The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        ##### The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


##### Useless evaluation function. If player X uses this he will definitely lose!
def random_eval(board):
  return random.randint(-100, 100)


def my_evaluate_board(board):
    if has_won(board, "X"):
        return float("Inf")
    elif has_won(board, "O"):
        return -float("Inf")
    else:
        """
        If the game isnt over, a good strategy would be to have more streaks of two or streaks of three than your opponent. Having these streaks means that youre closer to getting a streak of four and winning the game!

        One of the trickiest part of counting streaks is that they can happen in eight different directions  up, up-right, right, down-right, down, down-left, left, and up-left.

        For now, lets just keep track of streaks to the right.
        """
    x_two_streak = 0
    o_two_streak = 0
    ##### Now we want to loop through every space on the board and see if theres the same symbol to the right. As this loop runs, well look through each piece of the board starting at the top of the left-most column. The loop will go down that column until it reaches the bottom of the board and then jumps to the top of the second column. One thing to note is that we dont want to check the final column, because that column doesnt have a column to the right. So the outer for loop should actually look like this: for col in range(len(board) -1).
    for col in range(len(board) -1):
      for row in range(len(board[0])):
        if board[col][row] == 'X' and board[col + 1][row] == 'X':
            x_two_streak += 1
        elif board[col][row] == 'O' and board[col + 1][row] == 'O':
            o_two_streak += 1
    return x_two_streak - o_two_streak


##### Check the evaluation function
##### Create a new board
new_board = make_board()
##### Make a few moves (X will be winning)
select_space(new_board, 1, 'X')
select_space(new_board, 1, 'O')
select_space(new_board, 2, 'X')
select_space(new_board, 3, 'O')
select_space(new_board, 4, 'X')
select_space(new_board, 7, 'O')
select_space(new_board, 5, 'X')
select_space(new_board, 5, 'O')
select_space(new_board, 6, 'X')
##### Visualise board
# print_board(new_board)
# print(my_evaluate_board(new_board))

##### Play!!!
two_ai_game()

"""
You have a good foundation for your evaluation function, but theres so much more you can do! Here are some ideas on how to expand your function:

Check for streaks in all eight directions.
Weight streaks of three higher than streaks of two.
Only count streaks if your opponent hasnt blocked the possibility of a Connect Four. For example, if theres an "X" streak of two to the right, but the next column over has an "O", then that streak is useless.
Only count streaks if theres enough board space to make a Connect Four. For example, theres no need to check for left streaks of two in the second column from the left. Even if there is a streak of two, you cant make a Connect Four going to the left, so the streak is useless.
Testing your evaluation function on test boards is critically important before plugging it into the two_ai_game() function. Make sure you know that your function is working how you expect it to before challenging our AI.
"""
