from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("\nYou win!\n")
        break
    guesses_left -= 1
else:
    print("\nYou lose.\n")
