import random

class Calcul():

    def rand(self, low, high):
        return random.randint(low, high)

    def is_in_range(self, number, smaller, bigger):
        return number > smaller and number < bigger