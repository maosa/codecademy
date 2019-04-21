##### MINIMAX

"""
>>>>> Games as Trees

Have you ever played a game against someone and felt like they were always two steps ahead? No matter what clever move you tried, they had somehow envisioned it and had the perfect counterattack. This concept of thinking ahead is the central idea behind the minimax algorithm.

The minimax algorithm is a decision-making algorithm that is used for finding the best move in a two player game. It’s a recursive algorithm — it calls itself. In order for us to determine if making move A is a good idea, we need to think about what our opponent would do if we made that move.

We’d guess what our opponent would do by running the minimax algorithm from our opponent’s point of view. In the hypothetical world where we made move A, what would they do? Surely they want to win as badly as we do, so they’d evaluate the strength of their move by thinking about what we would do if they made move B.

As this process repeats, we can start to make a tree of these hypothetical game states. We’ll eventually reach a point where the game is over — we’ll reach a leaf of the tree. Either we won, our opponent won, or it was a tie. At this point, the recursion can stop. Because the game is over, we no longer need to think about how our opponent would react if we reached this point of the game.
"""

##### Examine tic_tac_toe.py functions

from tic_tac_toe import *

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

print_board(my_board)

print(available_moves(my_board), '\n')

select_space(my_board, 5, 'O')

print_board(my_board)

select_space(my_board, 9, 'X')
select_space(my_board, 6, 'O')

print(available_moves(my_board), '\n')

select_space(my_board, 7, 'X')
select_space(my_board, 2, 'O')
select_space(my_board, 8, 'X')

print_board(my_board)

print('X won:', has_won(my_board, 'X'))
print('O won:', has_won(my_board, 'O'))

"""
>>>>> Detecting Tic-Tac-Toe Leaves

An essential step in the minimax function is evaluating the strength of a leaf. If the game gets to a certain leaf, we want to know if that was a better outcome for player "X" or for player "O".

Here’s one potential evaluation function: a leaf where player "X" wins evaluates to a 1, a leaf where player "O" wins evaluates to a -1, and a leaf that is a tie evaluates to 0.
"""
