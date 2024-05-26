class Human:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return "Person's name is " + str(self.name)

    def get_age(self):
        return "Person's age is " + str(self.age)

    def get_gender(self):
        return "Person's gender is " + str(self.gender)

    def print_full_info(self):
        print("Person: " + str(self.name))
        print("Age: " + str(self.age))
        print("Gender: " + str(self.gender))


human_1 = Human(name="Nick", age=35, gender="Man")

human_1.print_full_info()
print(human_1.get_age())
print(human_1.age)
