# __author__ = "Matt Andersen"
#
# VOWELS = "aeiou"
#
# with open("english_dictionary.txt", 'r') as in_file:
#     # Keep a total count of all words that meet the criteria
#     total_word_count = 0
#
#     # Begin the loop - loop through all ~350k words in this English dictionary
#     for word in in_file:
#         # Strip the new line character from the words in the dictionary
#         word = word.strip()
#         # Initialise an empty variable that will store all the vowels found in a word
#         vowel_structure = ""
#         # Loop through all the characters in each word
#         for char in word:
#             # If a character is a vowel, it will be concatenated to the 'vowel_structure' variable
#             if char in VOWELS:
#                 vowel_structure += char
#         # If the vowels found in the word match VOWELS exactly then print this word
#         # Also increase the 'total_word_count' by 1
#         if vowel_structure == VOWELS:
#             print(word)
#             total_word_count += 1
#
#     print("\nTotal words: " + str(total_word_count))

# import datetime
#
# __author__ = 'Angus Freudenberg'
#
#
# class Person:
#
#     def __init__(self, name="", gender="", dob=""):
#         self.name = name
#         self.gender = gender
#         self.dob = dob
#
#     def __str__(self):
#         return '{} is a {}. {} is {} years old'.format(self.name,
#                                                     'Male' if self.gender.upper() == "M" else 'Female',
#                                                     'He' if self.gender.upper() == "M" else 'She',
#                                                     str(self.get_age()))
#
#     def get_age(self):
#         dob_year = self.dob[-4:]
#         age = int(datetime.datetime.today().year) - int(dob_year)
#         return age
#
# if __name__ == '__main__':
#     angus = Person('Angus', 'M', '18/11/1994')
#     print(angus)
#
#     jane = Person('Jane', 'F', '12/03/1985')
#     print(jane)


with open("english_dictionary.txt", 'r') as in_file, open("20As.txt", 'w') as out_file:
    count = 0
    for word in in_file:
        if word[0] == "a" and count < 20:
            out_file.write(word)
            count += 1