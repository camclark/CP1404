# def count_down(i):
#     print(i)
#     if i < 1:
#         return
#     else:
#         count_down(i-1)
#
#
# def spell_word(str):
#     if len(str) < 1:
#         return
#     else:
#         spell_word(str[0:-1])
#         print(str[-1])
# count_down(10)
# spell_word("big dps")

#
# def spell_word_inside_out(word):
#     if len(word) < 1:
#         return
#
#     if len(word) % 2 == 0:
#         print(word[-1], end=" ")
#         spell_word_inside_out(word[0:-1])
#
#     else:
#         print(word[0], end=" ")
#         spell_word_inside_out(word[1:])
#
# spell_word_inside_out("Programming")


def spell_word_inside_out_v2(word):
    if len(word) < 2:
        return word

    return (word[0] + word[-1]) + spell_word_inside_out_v2(word[1:-1])

print(spell_word_inside_out_v2("Programming"))

# def ispalindrome(word):
#     return word == word[::-1]

# def ispalindrome(word):
#     if len(word) < 2:
#         return True
#     if word[0] != word[-1]:
#         return False
#     print(word)
#     return ispalindrome(word[1:-1])
#
#
# print(ispalindrome("saippuakivikauppias"))