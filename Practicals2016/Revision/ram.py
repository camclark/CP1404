# naughty = ["boobies", "vagina", "meathose"]
#
# with open("wishlist.txt", "r+") as in_file:
#     next(in_file)
#     for line in in_file:
#         if line in naughty:
#             with open("wishlist.txt", "w") as out_file:
#                 out_file.write("coal")

# class Person:
#     def __init__(self, name, gender, birthday):
#         self.name = name
#         self.gender = gender
#         self.birthday = birthday
#
#     def name_change(self):
#         self.name = "CHANGED"
#
#     def __str__(self):
#         return "{}".format(self.name)
#
#
# class Dancer(Person):
#     def __init__(self, name, gender, birthday):
#         super().__init__(name, gender, birthday)
#
# a = Dancer("dude", "m", "8/2/3")
# print(a)
# a.name_change()
# print(a)

# class Stress:
#     def __init__(self, cause="", rating = 0, solution=""):
#         self.cause = cause
#         self.rating = rating
#         self.solution = solution
#
#     def __str__(self):
#         return "The cause of my stress is {}. I will {}.".format(self.cause, self.solution)
#
#     def destress(self):
#         return "Look at some cute dog pics instead!"
#
#     def get_rating_description(self):
#         if self.rating <= 5:
#             return "Pretty chill, got things under control"
#         elif self.rating > 5 and self.rating <= 10:
#             return "DO NOT PANIC, U CAN DO IT"
#         elif self.rating > 10:
#             return "YOU HAVE reached maxIMUM CAPACITY AAAAAAAAAAAA"
#         else:
#             return "sup"
#
#     def do_study(self):
#         self.rating = 100

# def main():
#     try:
#         exam = 0("this programming exam", 10345034589, "probably just crawl into a hole and die")
#         print(exam)
#
#         print(exam.destress(), exam.get_rating_description())
#     except NameError:
#         print("LOL")
#
# main()
S = [1, 2, 3, 4, 5, 6]
a = ("tuple",)
b = {"dict":"boys"}
c = ["list"]
M = [x for x in S if x % 2 == 0]

print(type(a))
print(type(b))
print(type(c))
print(M)

"""
d - debugger
i - interpreter
c - complilor
e - editor
"""
