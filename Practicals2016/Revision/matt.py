__author__ = "Matt Andersen"

VOWELS = "aeiou"

with open("english_dictionary.txt", 'r') as in_file:
    # Keep a total count of all words that meet the criteria
    total_word_count = 0

    # Begin the loop - loop through all ~350k words in this English dictionary
    for word in in_file:
        # Strip the new line character from the words in the dictionary
        word = word.strip()
        # Initialise an empty variable that will store all the vowels found in a word
        vowel_structure = ""
        # Loop through all the characters in each word
        for char in word:
            # If a character is a vowel, it will be concatenated to the 'vowel_structure' variable
            if char in VOWELS:
                vowel_structure += char
        # If the vowels found in the word match VOWELS exactly then print this word
        # Also increase the 'total_word_count' by 1
        if vowel_structure == VOWELS:
            print(word)
            total_word_count += 1

    print("\nTotal words: " + str(total_word_count))
