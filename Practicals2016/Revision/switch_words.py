"""
A program that takes a sentence and flips all the words while keeping them
in order
"""

print(" ".join([word[::-1] for word in "Greg was a great guy".split(" ")]))