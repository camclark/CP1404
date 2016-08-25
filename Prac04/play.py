def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Enter age: "))
            if age < 3 or age > 6:
                print("wot")
            else:
                print("good")

        except:
            print("Invalid not an interger")



main()