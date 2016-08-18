LOWER = 10
UPPER = 100

def main():
    character = input('please enter a character: ')
    print('The ASCII code for {} is {}'.format(character,ord(character)))

    get_number()


def get_number():
    number = int(input('please enter a number between 10 and 50: '))
    while number < 10 or number > 50:
        print('please enter a valid number!')
        number = int(input('please enter a number between 10 and 50: '))
    print('The character for {} is {}'.format(number, chr(number)))

main()