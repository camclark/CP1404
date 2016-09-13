"""
CP1404/CP5632 - Practical
"""
__author__ = 'Lindsay Ward'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_cel_to_fah(fahrenheit)
            print(celsius)
        elif choice == "F":
            celsius = float(input("Celsius: "))
            convert_fah_to_cel()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fah_to_cel(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return  celsius


def convert_cel_to_fah(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return  fahrenheit

main()
