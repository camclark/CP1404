class Person:
    def __init__(self, name, gender, birthday, favourite_colour):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.favourite_colour = favourite_colour

    def calc_age(self):
        """
        01/03/1995
        """
        day, month, year = self.birthday.split("/")
        month = int(month)
        year = int(year)
        if month <= 11:
            return 2016 - year
        else:
            return 2015 - year

    def pronoun(self):
        if self.gender.lower() == "m":
            return "he"
        elif self.gender.lower == "f":
            return "she"
        else:
            return "it"

    def __str__(self):
        return "{} is {}, {} was born on {}. Therefore {} is {}".format(self.name, self.gender, self.pronoun(),
                                                                        self.birthday, self.pronoun(), self.calc_age())


def main():
    cameron = Person("Cameron", "M", "7/1/1995", "Blue")
    pen_man = Person("pen man", "Pen", "7/1/1995", "Black")
    gilbert = Person("Daniel", "M", "29/12/1998", "Goon")

    print(cameron)
    print(pen_man)
    print(gilbert)


main()
