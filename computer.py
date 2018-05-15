import random
from player import Player


class Computer(Player):

    """Set number to the computer
    """

    def ask_for_number(self):
        number = 0

        while number < 1000:
            number = int(''.join(random.sample("0123456789", 4)))

        print "Computer number is {}".format(number)

        self.number = str(number)

    """Return boolean if the computer has won or not
    """

    def play_turn(self, number):
        guess = str(''.join(random.sample("0123456789", 4)))

        while int(guess) < 1000:
            guess = str(''.join(random.sample("0123456789", 4)))

        print "Computer guess number is: {}".format(guess)

        if self.bulls_and_cows(number, guess):
            print "The computer has won!"

            return True
        else:
            return False

    """Return name of the computer
    """

    def player_name(self):
        return "Computer"
