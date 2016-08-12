lower = 10
upper = 100
print("Enter a number ({}) - ({})".format(lower,upper))
for i in range(10, 120, 11):
    print("{:<4d} {}".format(i, chr(i)))