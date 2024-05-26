#  модифікатори доступу
# private -'__' - два підкреслювання перед змінною приватно для класу
# public,
# protected '_' - одне підкреслювання, приватно для пакету

class Worker:
    RIGHTS = "Every worker has right to get payed"\
        "for work he/she has done"

    def __init__(self, work_class):
        self.__class_salary_map = {  # private dict
            "A": 100,
            "B": 200,
            "C": 500,
            "D": 1000,
        }
        self.__salary = self.__calculate_salary(work_class)

    def __calculate_salary(self, work_class):
        return self.__class_salary_map.get(work_class, 0)

    @property  # open acsess to class atributes
    def salary(self):
        if not self.__salary:
            return "Undefined"
        return self.__salary


worker_1 = Worker(work_class="A")
print(worker_1.salary)
worker_2 = Worker(work_class="B")
print(worker_1.RIGHTS == worker_2.RIGHTS)  # True
print(Worker.RIGHTS)
