class Summarizer:
    def __init__(self, var_a, var_b):
        self.sum_a_b = self._get_sum(var_a, var_b)

    @staticmethod
    def _get_sum(var_a, var_b):
        return var_a+var_b


summarazer = Summarizer(var_a=10, var_b=5)
print(summarazer.sum_a_b)

######################################################


class Car:
    # Constructor
    def __init__(self, name, volume, color):
        self.engine = volume  # class atribute
        self.name = name  # class atribute
        self.color = color  # class atribute

    @staticmethod  # static method
    def ride():
        print('Driving...')

    @staticmethod  # static method
    def stop():
        print('Stoped')

    def get_info(self):
        print('Info\n==============')  # class method
        print('Name:', self.name)  # class method
        print('Color:', self.color)  # class method
        print('Engine:', self.engine)  # class method
        print('==============\n')  # class method


new_car = Car(name='some car', color='white', volume='3.5')

new_car.get_info()
