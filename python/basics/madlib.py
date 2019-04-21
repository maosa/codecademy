"""

This is a Codecademy project!!!

This program generates passages that are generated in mad-lib format
Author: Katherin

Steps needed to complete the game:
1) prompt the user for inputs
2) Print the story with the inputs in the right places

"""

# The template for the story

STORY = """This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."""

print("Welcome! Mad Libs program is now running")

name = input("Enter a name: ")

adj1 = input("Enter adjective number 1: ")

adj2 = input("Enter adjective number 2: ")

adj3 = input("Enter adjective number 3: ")

verb1 = input("Enter a verb: ")

noun1 = input("Enter noun number 1: ")

noun2 = input("Enter noun number 2: ")

animal = input("Choose an animal: ")

food = input("What did you last have for dinner? ")

fruit = input("Choose a fruit: ")

superhero = input("Who is your favourite superhero? ")

country = input("Which country were you born in? ")

dessert = input("Choose a dessert: ")

year = input("Add 100 year to your birth year: ")

print(STORY % (name, adj1, adj2, animal, food, verb1, noun1, fruit,
adj3, name, superhero, name, country, name, dessert, name, year, noun2))
