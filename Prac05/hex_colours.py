"""
CP1404/CP5632 Practical
Colour Hex values in a dictionary
"""

COLOUR_NAMES = {"f0f8ff": "AliceBlue", "000000": "Black", "5f9ea0": "CadetBlue", "d2691e": "Chocolate",
                "6495ed": "CornflowerBlue", "006400": "DarkGreen", "e9967a": "DarkSalmon"}

colour = input("Enter short colour: #").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: #").lower()

for hex_value, colour in COLOUR_NAMES.items():
    print("{:<5} is {:<10}".format(hex_value, colour))
