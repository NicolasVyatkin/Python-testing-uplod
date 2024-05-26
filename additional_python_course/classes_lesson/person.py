# Lesson 020 Creating classes

class Person():
    """Model of the person"""

    def __init__(self, name, age):
        """Initialization attributes of the person - name and age"""
        self.name = name
        self.age = age
        print("Person created")

    def sing(self):
        """Make person sing"""
        print(self.name + " is singing")

    def dance(self):
        """Make person dance"""
        print(self.name + " is dancing")


man = Person("Kolin", 30)
women = Person("Sveta", 28)
# print(man.name)

man.dance()
women.dance()