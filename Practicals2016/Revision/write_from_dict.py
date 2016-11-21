"""
Read the file "english_dictionary.txt" into a dictionary and save only the first 20 words starting with a (or less if not enough) to a file.
"""
# key = line in english_dictonary
# item = english word
a_dictionary_20 = {}

with open("english_dictionary.txt", "r") as in_file:
    for i, line in enumerate(in_file):
        if line[0].lower() == "a":
            a_dictionary_20[i+1] = line.strip()
            if len(a_dictionary_20) == 20:
                break

with open("new_dict.txt", "w") as out_file:
    for item in a_dictionary_20:
        out_file.write(a_dictionary_20[item] + "\n")


# d = {'key':'value'}
# print(d)
# >>>{'key': 'value'}
# d['mynewkey'] = 'mynewvalue'
# print (d)
# >>>{'mynewkey': 'mynewvalue', 'key': 'value'}