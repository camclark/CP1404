def block_step(n):
    if n >= 0:
        return n + block_step(n - 1)
    return 0


def main():
    rows = int(input("How many rows are in your 2D pyramid? : "))
    print(block_step(rows))


main()
