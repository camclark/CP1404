"""
CP1404/CP5632 Practical
Count same words from input
"""

words_to_count = input("Text: ")
words_to_count = words_to_count.split(" ")

counted_words = {}
longest_key = ""

for word in words_to_count:
    if word in counted_words:
        counted_words[word] += 1

    else:
        counted_words[word] = 1

        if len(word) > len(longest_key):
            longest_key = word

for word, word_count in counted_words.items():
    print("{:<{}} : {}".format(word, len(longest_key), word_count))
