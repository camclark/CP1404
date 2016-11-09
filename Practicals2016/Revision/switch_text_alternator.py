# My test:
# with open("switch.txt", "r+") as f:
#     if f.readline == "out": # list dont want that
#         text = "in"
#     else:
#         text = "out"
#
#     print(text, file=f)

# make grade print for ranges (P,C,D,HD)

# Given answer:

input_file = open("switch.txt")
contents = input_file.read()
input_file.close()

with open("switch.txt", "w") as out_file:
    if contents == "out":
        out_file.write("in")
        # print("in", file=out_file)
    else:
        out_file.write("out")
        # print("out", file=out_file)
