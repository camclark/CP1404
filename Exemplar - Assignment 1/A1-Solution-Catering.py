""" IT@JCU CP1200 Assignment 1 from 2014
    Catering Calculator - Solution
    Lindsay Ward
    18/02/2014 (modified 15/08/2015)

Pseudocode:

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6
PREMIUM_RATE = 1.25

function main()
    display welcome message
    display menu
    get choice
    while choice is not 'q'
        if choice is 'i'
            display instructions
        else if choice is 'c'
            call calculate_catering()
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


function calculate_catering()
    get number of adults
    while number of adults is < 0
        display error message
        get number of adults
    get number of children
    while number of children < 0
        display error message
        get number of children
    get service type
    while service type is not 'b' and service type is not 'p'
        display error message
        get service type

    cost = number of adults * COST_PER_HEAD + number of children * COST_PER_HEAD * CHILD_RATE
    service message = 'basic'
    if service type is 'p'
        cost = cost * PREMIUM_RATE
        service message = 'premium'
    if number of adults is 1
        adult message = 'adult'
    else
        adult message = 'adults'
    if number of children is 1
        child message = 'child'
    else
        child message = 'children'
    display cost, service type, number of adults, adult message, number of children, child message, service message

"""

COST_PER_HEAD = 10.0
CHILD_RATE = 0.6  # 60%
PREMIUM_RATE = 1.25
MENU = "\nMenu:\n(I)nstructions\n(C)alculate Catering\n(Q)uit"
INSTRUCTIONS = "Enter number of adults and children and choose a service type.\n\
Basic:   food only    = ${:.2f} per adult\n\
Premium: food & drink = ${:.2f} per adult\n\
Children are always {:.0%} of the price of adults.".format(COST_PER_HEAD, COST_PER_HEAD * PREMIUM_RATE, CHILD_RATE)


def main():
    """
    Catering Calculator program,
    calculate cost of catering package based on number of adults/children and package choice
    """
    print("Welcome to the Great IT@JCU Catering Calculator!")
    print("Written by Lindsay Ward, February 2014")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "I":
            print(INSTRUCTIONS)
        elif choice == "C":
            calculate_catering()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using the Great IT@JCU Catering Calculator.")


def calculate_catering():
    """ get details for catering job; calculate costs based on inputs and constant rates; print results """
    number_of_adults = int(input("Please enter the number of adults: "))
    while number_of_adults < 0:
        print("Error. Please enter a number >= 0")
        number_of_adults = int(input("Please enter the number of adults: "))

    number_of_children = int(input("Please enter the number of children: "))
    while number_of_children < 0:
        print("Error. Please enter a number >= 0")
        number_of_children = int(input("Please enter the number of children: "))

    service_type = input("Would you like (B)asic or (P)remium service?: ").upper()
    while service_type not in ('B', 'P'):
        print("Error. Please enter B or P")
        service_type = input("Would you like (B)asic or (P)remium service?: ").upper()

    # calculate catering details
    cost = number_of_adults * COST_PER_HEAD + number_of_children * COST_PER_HEAD * CHILD_RATE
    service_message = "basic"
    if service_type == 'P':
        # multiply basic total cost by premium rate to get premium total
        cost *= PREMIUM_RATE
        service_message = "premium"

    # print results, after determining correct singular/plural words
    if number_of_adults == 1:
        adult_word = "adult"
    else:
        adult_word = "adults"
    if number_of_children == 1:
        child_word = "child"
    else:
        child_word = "children"
    print("\nThat will be ${:.2f} for the {} service for {} {} and {} {}. Enjoy!".format(cost, service_message,
                                                                                         number_of_adults, adult_word,
                                                                                         number_of_children,
                                                                                         child_word))


main()
