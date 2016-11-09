"""
Program that finds all the English language words that have the vowels 'a', 'e', 'i', 'o', and 'u' in sequence.
For example a word like 'facetious'
From file "english_dictionary.text"
"""

with open("english_dictionary.txt", "r") as in_file:
    words_with_vowels_in_sequence = []

    for word in in_file:
        a_switch = False
        e_switch = False
        i_switch = False
        o_switch = False
        u_switch = False

        for character in word:
            if character.lower() == "a":
                if a_switch:
                    a_switch = False
                    break
                else:
                    a_switch = True

            if character.lower() == "e":
                if a_switch:
                    if e_switch:
                        e_switch = False
                        break
                    else:
                        e_switch = True
                else:
                    break

            if character.lower() == "i":
                if e_switch:
                    if i_switch:
                        i_switch = False
                        break
                    else:
                        i_switch = True
                else:
                    break

            if character.lower() == "o":
                if i_switch:
                    if o_switch:
                        o_switch = False
                        break
                    else:
                        o_switch = True
                else:
                    break

            if character.lower() == "u":
                if i_switch:
                    if u_switch:
                        u_switch = False
                        break
                    else:
                        u_switch = True
                else:
                    break

        if a_switch and e_switch and i_switch and o_switch and u_switch:
            words_with_vowels_in_sequence.append(word.strip())

    print("There are {} words that meet your criteria, they are: \n {}".format(len(words_with_vowels_in_sequence),
                                                                               words_with_vowels_in_sequence))
