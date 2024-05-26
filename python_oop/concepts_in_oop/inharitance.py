class Parrent:
    def __init__(self, param_1) -> None:
        self.atribute = param_1

    def parrent_method(self):
        return self.atribute * 3


class Child(Parrent):
    def __init__(self, param_1, param_2) -> None:
        super().__init__(param_1)
        self.atribute_child = param_2

    def child_method(self):
        return self.atribute_child * 2


parent = Parrent('hi')
child = Child('hi!', 'hello!')

print(parent.parrent_method())
print(child.child_method())
print(child.parrent_method())

#####################################################


class Iterator:
    def __init__(self, array):
        self.array = array

    def iterate(self):
        res_list = []
        for element in self.array:
            res_list.append(element)
        print(res_list)


class BackIterator(Iterator):
    def iterate(self):
        res_list = []
        for element in self.array[::-1]:
            res_list.append(element)
        print(res_list)


my_list = list(range(0, 15, 3))

iterator = Iterator(my_list)
back_iterator = BackIterator(my_list)
iterator.iterate()
back_iterator.iterate()
