from random import randint
from faker import Faker
import random
from data.data import Person


faker_en = Faker('En')


def generated_person():
    """function that generates random person for test"""
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_adress=faker_en.address(),
        mobile_phone=faker_en.msisdn(),
        subject='English'
    )


def generated_file():
    path = rf'G:\Python\PycharmProjects\selenium\selinium_test_demoqa_stud_reg_form\test{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(10,100)}')
    file.close()
    return path
