from person import Person


class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.nickname = nickname

vmi = Mentor("józsi")

