from base_person import *


class Warrior(Person):
    """Creating warrior class"""

    def __init__(self, name, age, weigh, high):
        """Initializing attributes of the supper clas"""
        super().__init__(name, age, weigh, high)
        self.rage = 100

    def get_rage(self):
        """Getting warriors rage"""
        print(self.name + " has warriors rage in quantity of " + str(self.rage))

    def description_person(self):
        """Overriding a parent class method"""
        description = "My name is " + self.name + " I am " + str(self.age) + " my rage quantity is " + str(self.rage)
        print(description)
        # return description
