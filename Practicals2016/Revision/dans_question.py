"""
a program that takes a sentence that flips all the words while keeping them in order,
for example "Greg was a great guy" comes out as "gerG saw a taerg yug"
"""

def word_flip(s):

    if len(s) == 1:
        print(s[0], end="")
        return

    word_flip(s[1:])
    print(s[0], end="")


def main(s):

    for word in s.split():
        word_flip(word)
        print(" ", end="")

main("Greg was as great guy")