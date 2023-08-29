# Вычисление объёма цилиндра по средством нескольких функций

import math

PI = math.pi


def radius():
    n = float(input('Please enter the diameter of the cylinder cm: '))
    n /= 2
    return n


def high():
    h = float(input('Please enter the high of the cylinder cm: '))
    return h


def volume():
    r = radius()
    h = high()
    s = PI * r ** 2
    v = s * h
    return v


print('The volume of the cylinder with parameters you typed is ', round(volume(), 2), ' sm3')

def mass(g):
    m = float(input("Please enter the mass of the cylinder's g/cm3: "))
    calc=g*m/1000
    return calc
print('Mass of the cylinder in kg is - ',round(mass(volume()),2))