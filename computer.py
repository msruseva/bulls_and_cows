import random
from player import Player


class Computer(Player):

    def __init__(self):
        self.number = self.generate_number()

    def generate_number(self):
        number = 0

        while number < 1000:
            number = int(''.join(random.sample("0123456789", 4)))

        print "Computer number is {}".format(number)

        return str(number)

    def make_a_guess(self):
        guess = str(''.join(random.sample("0123456789", 4)))

        print "Computer guess number is: {}".format(guess)

        return guess
