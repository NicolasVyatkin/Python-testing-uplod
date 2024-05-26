########## Realization datails ################
print('######### first example #######')


class Core:
    def __init__(self):
        self._types = {
            'A': 100,
            'B': 300,
        }

    def get_salary(self, worker_type):
        return self._types.get(worker_type, 0)

########## User interfase ################


class AccountingInterfasce:
    def __init__(self, data):
        self._core = Core()
        self._people_class_dict = data

    def get_person_salary(self, name):
        person_class = self._people_class_dict.get(name)
        return self._core.get_salary(person_class)

########## Start ################


database = {'John': 'A', 'Sarah': 'B', }
accounting = AccountingInterfasce(data=database)
print('Jons salary: ', accounting.get_person_salary('John'))
#############################################################
print('######### second example #######')


class CatPurr:
    def __init__(self):
        self.__mood_purr_map = {
            'very good': 'Loud',
            'good': 'Medium',
            'normal': 'Soft',
        }
        self.__purr_types = {
            'Loud': 'PUUURRRRR!!!!!!!',
            'Medium': 'Puurrr...Purrr',
            'Soft': 'purr..purr..purr',
        }

    def _define_purr_type_by_mood(self, mood):
        return self.__mood_purr_map.get(mood)

    def _make_purr(self, purr_type):
        return self.__purr_types.get(purr_type)

    def purr(self, mood):
        return self._make_purr(self._define_purr_type_by_mood(mood))


class Cat:
    def __init__(self):
        self.__purr_machanism = CatPurr()
        self.__mood = 'normal'

    def know_cat_feelings(self):
        print(self.__purr_machanism.purr(self.__mood))

    def give_food(self):
        if self.__mood == 'normal':
            self.__mood = 'good'
        elif self.__mood == 'good':
            self.__mood = 'very good'
        else:
            self.__mood = 'very good'


cat = Cat()
print(cat.know_cat_feelings())
cat.give_food()
print(cat.know_cat_feelings())
cat.give_food()
print(cat.know_cat_feelings())
