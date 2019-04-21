"""

This is a Codecademy project!

In this project, we’ll create a calculator that can compute the area of the following shapes:

- Circle
- Triangle

The program should do the following:

1) Prompt the user to select a shape.
2) Calculate the area of that shape.
3) Print the area of that shape to the user.

Let’s begin!

"""

print("\nWelcome! Area calculator is now running!\n")

option = input("Enter C for Circle or T for Triangle: ")

if option == "C":

  radius = float(input("What's your circle's radius? "))

  area = 3.14159 * (radius**2)

  print("\nArea: " + str(area) + " squared units")

elif option == "T":

  base = float(input("How big is your triangle's base? "))

  height = float(input("What's your triangle's height? "))

  area = 0.5 * base * height

  print("\nArea: " + str(area) + " squared units")

else:
  print("\nCheck your input!!!\n")

print("\nThanks for using AreaCalculator. See you soon!\n")
