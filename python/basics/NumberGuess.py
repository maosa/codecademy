"""

In this project, well build a program that rolls a pair of dice and asks the user to guess the sum. If the users guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.

The program should do the following:

1) Roll a pair of dice.
2) Add the values of the roll.
3) Ask the user to guess a number.
4) Compare the users guess to the total value.
5) Determine the winner (user or computer).

"""

from random import randint
from time import sleep


def get_user_guess():
  guess = int(input("What's your guess? \n"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("\nThe maximum possible value is: %d\n" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("\nInvalid guess...You surpassed the maximum allowable value!\n")
  else:
    print("\nRolling...")
    sleep(2)
    print("First roll is %d" % first_roll)
    sleep(1)
    print("Second roll is %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("\nCongratulations! You won!\n")
    else:
      print("\nI'm sorry...you lost. The computer won!\n")

roll_dice(6)
