"""
In our first lesson on the minimax algorithm, we wrote a program that could play the perfect game of Tic-Tac-Toe. Our AI looked at all possible future moves and chose the one that would be most beneficial. This was a viable strategy because Tic Tac Toe is a small enough game that it wouldn’t take too long to reach the leaves of the game tree.

However, there are games, like Chess, that have much larger trees. There are 20 different options for the first move in Chess, compared to 9 in Tic-Tac-Toe. On top of that, the number of possible moves often increases as a chess game progresses. Traversing to the leaves of a Chess tree simply takes too much computational power.

In this lesson, we’ll investigate two techniques to solve this problem. The first technique puts a hard limit on how far down the tree you allow the algorithm to go. The second technique uses a clever trick called pruning to avoid exploring parts of the tree that we know will be useless.

Before we dive in, let’s look at the tree of a more complicated game — Connect Four!

If you’ve never played Connect Four before, the goal is to get a streak of four of your pieces in any direction — horizontally, vertically, or diagonally. You can place a piece by picking a column. The piece will fall to the lowest available row in that column.
"""

from connect_four import *

print_board(half_done)

##### This will show you the number of game states in the tree, assuming half_done is the root of the tree and it is "X"s turn.
print(tree_size(half_done, 'X'))

##### Lets make a move and see how the size of the tree changes.
select_space(half_done, 6, 'X')

##### Since "X" has taken their turn, it is now "O"s turn.
print(tree_size(half_done, 'O'))

"""
>>>>> Depth and Base Case

The first strategy we’ll use to handle these enormous trees is stopping the recursion early. There’s no need to go all the way to the leaves! We’ll just look a few moves ahead.

Being able to stop before reaching the leaves is critically important for the efficiency of this algorithm. It could take literal days to reach the leaves of a game of chess. Stopping after only a few levels limits the algorithm’s understanding of the game, but it makes the runtime realistic.

In order to implement this, we’ll add another parameter to our function called depth. Every time we make a recursive call, we’ll decrease depth by 1.

We’ll also have to edit our base case condition. We now want to stop if the game is over (we’ve hit a leaf), or if depth is 0.
"""

from connect_four import *
import random
random.seed(108)

new_board = make_board()

##### Add a third parameter named depth
def minimax(input_board, is_maximizing, depth):
    ##### Change this if statement to also check to see if depth = 0
    if game_is_over(input_board) or depth == 0:
        return [evaluate_board(input_board), ""]
    best_move = ""
    if is_maximizing == True:
        best_value = -float("Inf")
        symbol = "X"
    else:
        best_value = float("Inf")
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        ##### Add a third parameter to this recursive call
        hypothetical_value = minimax(new_board, not is_maximizing, depth - 1)[0]
        if is_maximizing == True and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
        if is_maximizing == False and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
    return [best_value, best_move]

##### The first is the value of the best possible move, and the second is the move itself.
print(minimax(new_board, True, 3))

"""
>>>>> Evaluation Function

By adding the depth parameter to our function, we’ve prevented it from spending days trying to reach the end of the tree. But we still have a problem: our evaluation function doesn’t know what to do if we’re not at a leaf. Right now, we’re returning positive infinity if Player 1 has won, negative infinity if Player 2 has won, and 0 otherwise. Unfortunately, since we’re not making it to the leaves of the board, neither player has won and we’re always returning 0. We need to rewrite our evaluation function.

Writing an evaluation function takes knowledge about the game you’re playing. It is the part of the code where a programmer can infuse their creativity into their AI. If you’re playing Chess, your evaluation function could count the difference between the number of pieces each player owns. For example, if white had 15 pieces, and black had 10 pieces, the evaluation function would return 5. This evaluation function would make an AI that prioritizes capturing pieces above all else.

You could go even further — some pieces might be more valuable than others. Your evaluation function could keep track of the value of each piece to see who is ahead. This evaluation function would create an AI that might really try to protect their queen. You could even start finding more abstract ways to value a game state. Maybe the position of each piece on a Chess board tells you something about who is winning.

It’s up to you to define what you value in a game. These evaluation functions could be incredibly complex. If the maximizing player is winning (by your definition of what it means to be winning), then the evaluation function should return something greater than 0. If the minimizing player is winning, then the evaluation function should return something less than 0.

>>>>> Alpha-Beta Pruning

By writing an evaluation function that works on non-leaf game states, we can stop the recursion early. But in a perfect world, we’d still want to reach the leaves of the tree. In order to traverse farther down the tree without dramatically increasing the runtime, we can implement a technique called alpha-beta pruning.

The core idea behind alpha-beta pruning is to ignore parts of the tree that we know will be dead ends.

>>>>> Implement Alpha-Beta Pruning

Alpha-beta pruning is accomplished by keeping track of two variables for each node — alpha and beta. alpha keeps track of the minimum score the maximizing player can possibly get. It starts at negative infinity and gets updated as that minimum score increases.

On the other hand, beta represents the maximum score the minimizing player can possibly get. It starts at positive infinity and will decrease as that maximum possible score decreases.

For any node, if alpha is greater than or equal to beta, that means that we can stop looking through that node’s children.

To implement this in our code, we’ll have to include two new parameters in our function — alpha and beta. When we first call minimax() we’ll set alpha to negative infinity and beta to positive infinity.

We also want to make sure we pass alpha and beta into our recursive calls. We’re passing these two values down the tree.

Next, we want to check to see if we should reset alpha and beta. In the maximizing case, we want to reset alpha if the newly found best_value is greater than alpha. In the minimizing case, we want to reset beta if best_value is less than beta.

Finally, after resetting alpha and beta, we want to check to see if we can prune. If alpha is greater than or equal to beta, we can break and stop looking through the other potential moves.
"""

from connect_four import *
import random
random.seed(108)

def minimax(input_board, is_maximizing, depth, alpha, beta):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board) or depth == 0:
        return [evaluate_board(input_board), "", alpha, beta]
    best_move = ""
    if is_maximizing == True:
        best_value = -float("Inf")
        symbol = "X"
    else:
        best_value = float("Inf")
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        hypothetical_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)[0]
        if is_maximizing == True and hypothetical_value > best_value:
            best_value = hypothetical_value
            alpha = max(alpha, best_value)
            best_move = move
        if is_maximizing == False and hypothetical_value < best_value:
            best_value = hypothetical_value
            beta = min(beta, best_value)
            best_move = move
        if alpha >= beta:
            break
    return [best_value, best_move, alpha, beta]

print_board(board)
print(minimax(board, True, 6, -float('Inf'), float('Inf')))

"""
>>>>> Review

Great work! We’ve now edited our minimax() function to work with games that are more complicated than Tic Tac Toe. The core of the algorithm is identical, but we’ve added two major improvements:

We wrote an evaluation function specific to our understanding of the game (in this case, Connect Four). This evaluation function allows us to stop the recursion before reaching the leaves of the game tree.
We implemented alpha-beta pruning. By cleverly detecting useless sections of the game tree, we’re able to ignore those sections and therefore look farther down the tree.
Now’s our chance to put it all together. We’ve written most of the function two_ai_game() which sets up a game of Connect Four played by two AIs. For each player, you need to call fill in the third parameter of their minimax() call.

Remember, right now our evaluation function is using a pretty bad strategy. An AI using the evaluation function we wrote will prioritize making sure its pieces are the top pieces of each column.

Fill in the third parameter of both minimax() function calls. This parameter is the depth of the recursive call. The higher the number, the “smarter” the AI will be.

What happens if they have equal intelligence? What happens if one is significantly smarter than the other?

We suggest keeping these parameters under 7. Anything higher and the program will take a while to complete!
"""

from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      # Fill in the third parameter for the first player's "intelligence"
      result = minimax(my_board, True, 6, -float("Inf"), float("Inf"))
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #Fill in the third parameter for the second player's "intelligence"
        result = minimax(my_board, False, 5, -float("Inf"), float("Inf"))
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

two_ai_game()
