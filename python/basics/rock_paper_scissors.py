"""

In this project, we’ll build Rock-Paper-Scissors!

The program should do the following:

1) Prompt the user to select either Rock, Paper, or Scissors.
2) Instruct the computer to randomly select either Rock, Paper, or Scissors.
3) Compare the user’s choice and the computer’s choice.
4) Determine a winner (the user or the computer).
5) Inform the user who the winner is.

"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie":"Yawn it's a tie!", "won":"Yay you won!", "lost":"Aww you lost!"}

def decide_winner(user_choice, computer_choice):
    print("User's choice: %s\nComputer's choice: %s\n" % (user_choice, computer_choice))
    if user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print(message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print(message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print(message["won"])
    else:
        print(message["lost"])

def play_RPS():
    user_choice = input("\nEnter Rock, Paper, or Scissors: \n")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

play_RPS()
