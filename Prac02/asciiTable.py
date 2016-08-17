lower = 10
upper = 100
print("Enter a number ({}) - ({})".format(lower,upper))
for i in range(34, 127, 1):
    print("{:<4d} {}".format(i, chr(i)))