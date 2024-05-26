"""# Lesson 021-22 Creating Class Instances"""

# class Person():
#     """Creatind a person"""
#
#     def __init__(self, name, age, weigh, high):
#         """Initializing attributes of the person"""
#         self.age = age
#         self.name = name
#         self.high = high
#         self.weigh = weigh
#
#     def description_person(self):
#         """Person description"""
#         description = "My name is " + self.name + " I am " + str(self.age) + " y.o. my weigh is " + str(
#             self.weigh) + " and my high is " + str(self.high)
#         print(description)
#
#     def get_weigh(self):
#         """Getting persons weigh"""
#         print("Weigh of person named " + self.name + " is " + str(self.weigh) + " kg.")
#
#     def update_weigh(self):
#         """Chenging persons weigh"""
#         kg = int(input("Please enter your weigh: "))
#         self.weigh = kg
#
#     def update_weigh_v2(self, kg):
#         """Chenging persons weigh"""
#         self.weigh = kg


# man = Person("Kolin", 30, 80, 180)
# man.description_person()
#
# man.get_weigh()
# man.update_weigh()
# man.get_weigh()
# man.update_weigh_v2(120)
# man.get_weigh()

#########################"""Lesson 022 Class inheritance"""##########################################


# class Warrior(Person):
#     """Creating warrior class"""
#
#     def __init__(self, name, age, weigh, high):
#         """Initializing attributes of the supper clas"""
#         super().__init__(name, age, weigh, high)
#         self.rage = 100
#
#     def get_rage(self):
#         """Getting warriors rage"""
#         print(self.name + " has warriors rage in quantity of " + str(self.rage))
#
#     def description_person(self):
#         """Overriding a parent class method"""
#         description = "My name is " + self.name + " I am " + str(self.age) + " my rage quantity is " + str(self.rage)
#         # print(description)
#         return description

#
# # warrior = Warrior("Ronan", 32, 220, 200)
# warrior.update_weigh_v2(170)
# # warrior.description_person()
# # warrior.get_rage()
#
# # warrior.description_person()
# """or"""
# print(warrior.description_person())
