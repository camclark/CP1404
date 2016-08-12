import math

x = int(input('Please enter a number to be x'))
y = int(input('Please enter a number to be y'))


menu = '\nMain menu\n(1)Show the even numbers from x to y \n(2)Show the odd numbers from x to y\n(3)Show the squares from x to y \n(4)Exit the program\n'
print(menu)
menu_choice = input(">>> ").upper()
while menu_choice != '4':
    counter = False
    if menu_choice == '1':
        for number in range (x+1,y,1):
            if number%2 == 0:
                print(number, end=' ')
                counter = True
        if counter == False:
            print('There are no even numbers between', x, 'and', y)
    elif menu_choice == '2':
        for number in range (x+1,y,1):
            if number%2 == 1:
                print(number, end=' ')
                counter = True
        if counter == False:
            print('There are no odd numbers between', x, 'and', y)
    elif menu_choice == '3':
        for number in range(x + 1, y, 1):
            is_square_check = math.sqrt(number)
            if (is_square_check).is_integer():
                print(number, end=' ')
                counter = True
        if counter == False:
            print('There are no square numbers between', x, 'and', y)
    else:
        print('Input not recognised')
    print(menu)
    menu_choice = input(">>> ").upper()
print('Mission complete')