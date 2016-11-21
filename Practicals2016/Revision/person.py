from datetime import date


class Person:
    def __init__(self, name, gender, birthday):
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def calc_age(self):
        """
        01/03/1995
        """
        day, month, year = self.birthday.split("/")
        day, month, year = int(day), int(month), int(year)

        # Have they had their birthday this year?
        if month <= date.today().month and day <= date.today().day:
            return 2016 - year
        else:
            return 2015 - year

    def pronoun(self):
        if self.gender.lower() == "m":
            return "he"
        elif self.gender.lower() == "f":
            return "she"
        else:
            return "it"

    def __str__(self):
        return "{} is {}, {} was born on {}. Therefore {} is {}".format(name, self.gender, self.pronoun(),
                                                                        self.birthday, self.pronoun(), self.calc_age())


def main():
    print(Person("Cameron", "M", "7/1/1995"))
    print(Person("pen man", "Pen", "7/1/1995"))
    print(Person("Daniel", "M", "29/12/1998"))
    print(Person("Baby Danni", "F", "11/12/2015"))

main()
