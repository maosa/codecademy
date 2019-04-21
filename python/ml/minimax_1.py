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

from tic_tac_toe import *

start_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

x_won = [
	["X", "O", "3"],
	["4", "X", "O"],
	["7", "8", "X"]
]

o_won = [
	["O", "X", "3"],
	["O", "X", "X"],
	["O", "8", "9"]
]

tie = [
	["X", "X", "O"],
	["O", "O", "X"],
	["X", "O", "X"]
]

##### Create a function called game_is_over() that takes a board as a parameter. The function should return True if the game is over and False otherwise.
def game_is_over(board):
	return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

print(game_is_over(start_board))
print(game_is_over(x_won))
print(game_is_over(o_won))
print(game_is_over(tie))

##### Lets write another function called evaluate_board() that takes board as a parameter. This function will only ever be called if weve detected the game is over. The function should return a 1 if "X" won, a -1 if "O" won, and a 0 otherwise.
def evaluate_board(board):
	if has_won(board, 'X'):
		return 1
	elif has_won(board, 'O'):
		return -1
	else:
		return 0


if game_is_over(start_board):
	print(evaluate_board(start_board))

if game_is_over(x_won):
	print(evaluate_board(x_won))

if game_is_over(o_won):
	print(evaluate_board(o_won))

if game_is_over(tie):
	print(evaluate_board(tie))

"""
>>>>> Evaluating Leaves

We now know that we can evaluate the leaves of a game tree, but how does that help us? How are we going to use those values to find the best possible move for a game state that isn’t a leaf?

Let’s imagine a situation where you’re playing as the "X" player in a game of Tic-Tac-Toe and the game is almost over. The game board isn’t a leaf but it’s close. You have three possible moves. All three moves will immediately end the game — each of those future boards will be leaves.

Let’s say picking move A will result in you winning and moves B and C will each result in a tie. You’d clearly pick move A.

By picking move A, you’ve picked the move that led to the board with the highest value. You were picking between a 1 (an "X" win) or two 0s (the moves that would lead to a tie). Because you picked the move with the highest value, we can say that "X" is the maximizing player.

Let’s say you were playing a the "O" player under the same circumstances. Picking move A would somehow immediately lead to "X" winning, while moves B and C would lead to a tie. You’d pick one of the boards that would lead to a tie. "O" is the minimizing player. You would love to pick a board with the value of -1 (an "O" win), but unfortunately, that board doesn’t exist. You’ll have to settle with picking a board with the value of 0. At least you prevent "X" from winning.

>>>>> Copying Boards

One of the central ideas behind the minimax algorithm is the idea of exploring future hypothetical board states. Essentially, we’re saying if we were to make this move, what would happen. As a result, as we’re implementing this algorithm in our code, we don’t want to actually make our move on the board. We want to make a copy of the board and make the move on that one.

If we want to create a copy of our board our first instinct might be to do something like this

new_board = my_board

This won’t work the way we want it to! Python objects are saved in memory, and variables point to a location in memory. In this case, new_board, and my_board are two variables that point to the same object in memory. If you change a value in one, it will change in the other because they’re both pointing to the same object.

One way to solve this problem is to use the deepcopy() function from Python’s copy library.

new_board = deepcopy(my_board)

new_board is now a copy of my_board in a different place in memory. When we change a value in new_board, the values in my_board will stay the same!

>>>>> The Minimax Function

We’re now ready to dive in and write our minimax() function. The result of this function will be the “value” of the best possible move. In other words, if the function returns a 1, that means a move exists that guarantees that "X" will win. If the function returns a -1, that means that there’s nothing that "X" can do to prevent "O" from winning. If the function returns a 0, then the best "X" can do is force a tie (assuming "O" doesn’t make a mistake).

Our minimax() function has two parameters. The first is the game state that we’re interested in finding the best move. When the minimax() function first gets called, this parameter is the current state of the game. We’re asking “what is the best move for the current player right now?”

The second parameter is a boolean named is_maximizing representing whose turn it is. If is_maximizing is True, then we know we’re working with the maximizing player. This means when we’re picking the “best” move from the list of moves, we’ll pick the move with the highest value. If is_maximizing is False, then we’re the minimizing player and want to pick the minimum value.
"""

##### User-defined minimax function
# def minimax(input_board, is_maximizing):
# 	##### Base case - the game is over, so we return the value of the board
# 	if game_is_over(input_board):
# 		return [evaluate_board(input_board), ""]
# 	##### The maximizing player
# 	if is_maximizing:
# 		##### The best value starts at the lowest possible value
# 		best_value = -float("Inf")
# 		best_move = ""
# 		##### Loop through all the available moves
# 		for move in available_moves(input_board):
# 			##### Make a copy of the board and apply the move to it
# 			new_board = deepcopy(input_board)
# 			select_space(new_board, move, "X")
# 			##### Recursively find your opponent's best move
# 			hypothetical_value = minimax(new_board, False)[0]
# 			##### Update best value if you found a better hypothetical value
# 			if hypothetical_value > best_value:
# 				best_value = hypothetical_value
# 				best_move = move
# 		return [best_value, best_move]
# 	##### The minimizing player
# 	else:
# 		##### The best value starts at the highest possible value
# 	    best_value = float("Inf")
# 	    best_move = ""
# 	    ##### Testing all potential moves
#     	for move in available_moves(input_board):
# 			##### Copying the board and making the move
# 	      	new_board = deepcopy(input_board)
# 	      	select_space(new_board, move, "O")
# 	      	##### Passing the new board back to the maximizing player
# 	      	hypothetical_value = minimax(new_board, True)[0]
# 	      	##### Keeping track of the best value seen so far
# 	      	if hypothetical_value < best_value:
#         		best_value = hypothetical_value
#         		best_move = move
# 		return [best_value, best_move]


"""
Amazing! Our minimax() function is now returning a list of [value, move]. move gives you the number you should pick to play an optimal game of Tic-Tac-Toe for any given game state.

This line of code instructs the AI to make a move as the "X" player:

select_space(my_board, minimax(my_board, True)[1], "X")

Take some time to play a game against the computer. If you’re playing with "X"s, make your move as "X", and then call minimax() on the board using is_maximizing = False. The second item in that list will tell you the AI’s move. You can then enter the move for the AI as "O", make your next move as "X", and call the minimax() function again to get the AI’s next move.

You can also try having two AIs play each other. If you uncomment the code at the bottom of the file, two AI will play each other until the game is over.
"""

my_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

while not game_is_over(my_board):
	select_space(my_board, minimax(my_board, True)[1], "X")
	print_board(my_board)
	if not game_is_over(my_board):
		select_space(my_board, minimax(my_board, False)[1], "O")
		print_board(my_board)

"""
Review
Nice work! You implemented the minimax algorithm to create an unbeatable Tic Tac Toe AI! Here are some major takeaways from this lesson.

- A game can be represented as a tree. The current state of the game is the root of the tree, and each potential move is a child of that node. The leaves of the tree are game states where the game has ended (either in a win or a tie).
- The minimax algorithm returns the best possible move for a given game state. It assumes that your opponent will also be using the minimax algorithm to determine their best move.
- Game states can be evaluated and given a specific score. This is relatively easy when the game is over — the score is usually a 1, -1 depending on who won. If the game is a tie, the score is usually a 0.
"""
