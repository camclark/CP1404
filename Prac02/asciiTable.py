LOWER = 10
UPPER = 100
print("Enter a number ({}) - ({})".format(LOWER, UPPER))
for i in range(34, 127, 1):
    print("{:<4d} {}".format(i, chr(i)))