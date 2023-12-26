# miles per gallon
import random


def fuel_tank():
    a = random.randint(10, 25)
    b = random.randint(200, 400)

    mpg = b // a
    return mpg


print(fuel_tank())
