def main():
    try:
        item_price = float(input("Price: "))
    except (TypeError, ValueError):
        print("Please enter a number")


main()
