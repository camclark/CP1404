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

"""
Write a function which removes every second 'a' from a string.
Use recursion if you want. (if it is possible) (edited)

e.g. alphabetical -> alphbetical
    or abracadabra -> abrcadbra
"""


def remove_2nd_a(string):
    first_a = False
    new_string = ""
    for letter in string:
        if letter == "a" and first_a:
            first_a = False
        elif letter == "a":
            first_a = True
            new_string += letter
        else:
            new_string += letter

    return new_string

print(remove_2nd_a("abracadabra"))
