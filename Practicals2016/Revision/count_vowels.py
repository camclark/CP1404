# with open("english_dictionary.txt", "r") as in_file:
#     a_count = 0
#     e_count = 0
#     i_count = 0
#     o_count = 0
#     u_count = 0
#
#     for line in in_file:
#         for character in line:
#             if character == "a":
#                 a_count += 1
#             elif character == "e":
#                 e_count += 1
#             elif character == "i":
#                 i_count += 1
#             elif character == "o":
#                 o_count += 1
#             elif character == "u":
#                 u_count += 1
#
# print(a_count)
# print(e_count)
# print(i_count)
# print(o_count)
# print(u_count)
#

with open("english_dictionary.txt", "r") as in_file:
    vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for line in in_file:
        for character in line:
            if character in vowel_count:
                vowel_count[character] += 1

highest_count = max(vowel_count.values())

for value in vowel_count:
    if vowel_count[value] == highest_count:
        print("{} {}".format(value, highest_count))


# highest_count = max(vowel_count.values())
# print("{} has the highest prevalence at  {}".format(vowel_count(highest_count), highest_count))




# with open("english_dictionary.txt", 'r') as dictionary_object:
#     VOWELS = dict(zip('aeiou', [0, 0, 0, 0, 0]))
#     print(VOWELS)
#     for word in dictionary_object:
#         for char in word:
#             if char in VOWELS:
#                 VOWELS[char] += 1
#     vowel_occurences_list = []
#     for vowel, occurences in VOWELS.items():
#         vowel_occurences_list.append((occurences, vowel))
#     vowel_occurences_list.sort(reverse=True)
#     for vowel, occurences in vowel_occurences_list:
#         print("{:12d} {:<3s}".format(vowel, occurences))
