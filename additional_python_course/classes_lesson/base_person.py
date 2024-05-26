class Person():
    """Creatind a person"""

    def __init__(self, name, age, weigh, high):
        """Initializing attributes of the person"""
        self.age = age
        self.name = name
        self.high = high
        self.weigh = weigh

    def description_person(self):
        """Person description"""
        description = "My name is " + self.name + " I am " + str(self.age) + " y.o. my weigh is " + str(
            self.weigh) + " and my high is " + str(self.high)
        print(description)

    def get_weigh(self):
        """Getting persons weigh"""
        print("Weigh of person named " + self.name + " is " + str(self.weigh) + " kg.")

    def update_weigh(self):
        """Chenging persons weigh"""
        kg = int(input("Please enter your weigh: "))
        self.weigh = kg

    def update_weigh_v2(self, kg):
        """Chenging persons weigh"""
        self.weigh = kg


