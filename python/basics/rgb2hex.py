"""

In this project, we’ll use Bitwise operators to build a calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

We’ll add three methods to the project:

1) A method to convert RGB to Hex
2) A method to convert Hex to RGB
3) A method that starts the prompt cycle

"""

def rgb_hex():

    invalid_msg = "\nInvalid RGB value!\n"

    red = int(input("Enter a value for red (R): "))
    if red < 0 or red > 255:
        print(invalid_msg)

    green = int(input("Enter a value for green (G): "))
    if green < 0 or green > 255:
        print(invalid_msg)

    blue = int(input("Enter a value for blue (B): "))
    if blue < 0 or blue > 255:
        print(invalid_msg)

    val = (red << 16) + (green << 8) + blue

    print("%s" % (hex(val)[2:]).upper())

def hex_rgb():

    hex_val = input("\nEnter a hexadecimal value: ")

    if len(hex_val) != 6:
        print("\nError!\nAn invalid hexadecimal value was entered!\n")
        return
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2**8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits

    print("\nRed: %s\nGreen: %s\nBlue: %s" %(red, green, blue))

def convert():
    while True:
        option = input("\nEnter 1 to convert RGB to HEX.\nEnter 2 to convert HEX to RGB.\nEnter X to Exit.\n")
        if option == "1":
            print("\nRGB to Hex...\n")
            rgb_hex()
        elif option == "2":
            print("\nHex to RGB...\n")
            hex_rgb()
        elif option == "X" or option == "x":
            break
        else:
            print("\nError!!!\n")

convert()
