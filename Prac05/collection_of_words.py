"""
CP1404/CP5632 Practical
Count same words from input
"""

words_to_count = input("Text: ")
words_to_count = words_to_count.split(" ")

counted_words = {}

for word in words_to_count:
    if word in counted_words:
        counted_words[word] += 1
    else:
        counted_words[word] = 1

for word,word_count in counted_words.items():
    print("{:<10} : {:>5}".format(word,word_count))