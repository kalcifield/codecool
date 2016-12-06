class Person:
    def __init__(self, first_name, last_name, year_of_birth, gender):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_birth = int(year_of_birth)
            self.gender = gender
        except ValueError:
            print("whoops, year of birth is wrong")

