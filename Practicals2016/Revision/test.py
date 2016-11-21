# def inside_out(word):
#     if len(word) < 2:
#         return word
#
#     return ("{} {} ".format(word[0], word[-1])) + inside_out(word[1:-1])
#
# print(inside_out(" "))


# def print_outside_in(text):
#     if text.strip() == "":
#         return
#     print(text[0], end=" ")
#
#     if len(text) > 1:
#         print(text[-1], end=" ")
#         print_outside_in(text[1:-1])
#
# print_outside_in("abba")

# """
# Write a function which removes every second 'a' from a string.
# Use recursion if you want. (if it is possible) (edited)
#
# e.g. alphabetical -> alphbetical
#     or abracadabra -> abrcadbra
# """
#
#
# def remove_2nd_a(string):
#     first_a = False
#     new_string = ""
#     for letter in string:
#         if letter == "a" and first_a:
#             first_a = False
#         elif letter == "a":
#             first_a = True
#             new_string += letter
#         else:
#             new_string += letter
#
#     return new_string
#
# print(remove_2nd_a("abracadabra"))

# def funcy(x, i):
#     return x[i]
#
# a = [i]
# b = funcy(a, 2)
# print(b)

# age = int(input("Please enter your age: "))
# for i in range(age, -1, -1):
#     print(i*i)

# """
# Write a function that takes two integer input parameters, adds up the numbers between these (inclusive)
# and returns the total. If the first number is not less than the second number it should return 0.
# Example if the parameters are (9, 11), it should return 30
# """
#
#
# def number_comparision(number_1, number_2):
#     if not number_1 < number_2:
#         return 0
#     else:
#         total = 0
#         for i in range(number_1, number_2+1, +1):
#             total += i
#         return total
#
# print(number_comparision(9, 11))

# s, t = "James Brown", ""
# for i in range(len(s)):
#     t += s[i - len(s)]
# print(t)

# a = [1, 2, 3]
# a.append(a[1])
# a.reverse()
# print(a)
#
# #output - [2, 3, 2, 1]

# def countWords(s):
#     count = 0
#     for word in s.split(" "):
#         count += 1
#     return count
#
# s = "This is a sentence with words in it"
#
# print(countWords(s)) #displays 8

# """
# 7. Write a function that takes in one integer parameter, n, and returns a list of n unique random numbers between 1 and 10 * n
# """
#
# from random import randint
#
# def unique_random_number_printer(interger):
#     for i in range(0, interger, 1):
#         print(randint(1,10))
#
# unique_random_number_printer(5)

# """
# 8. Write pseudocode for a program that asks the user for a string then displays every letter in the string twice.
# E.g. if they input "hello exam" it should display "hheelllloo  eexxaamm"
# """
#
#
# def repeat_letters(s):
#     new_s = ""
#     for char in s:
#         if char != " ":
#             new_s += char+char
#         else:
#             new_s += char
#     return new_s
#
# print(repeat_letters("hello exam"))

# """
# 9. Explain how a programmer would choose whether to use a while loop or a for loop and give examples of each.
#
# While loop:
# When the number of iterations between the start and the end point is unknown.
# Eg - having a while loop to exit from a menu
# while input != q:
#     options
#
# For loop:
# When there is a set known number of iterations
# eg - using a for loop to count from 1 to 10
# for i in range(1, 11, 1):
#     print i
# """

def backwards(s):
    if len(s) == 1:
        print(s)
        return

    backwards(s[1:])
    print(s[0], end="")

backwards("teehee im mature")