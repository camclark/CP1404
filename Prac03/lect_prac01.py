import string


def count_lower(text):
    count = 0

    for character in text.lower():
        if character in string.ascii_lowercase:
            count += 1
    return count


def main():
    print(count_lower("dudeD8"))

main()
