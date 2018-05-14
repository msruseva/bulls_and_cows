import pdb


class Player:

    def __init__(self):
        pass

    def bulls_and_cows(self, number, guess):
        bulls = 0
        cows = 0

        for digit in number:
            for guess_digit in guess:
                if digit == guess_digit and number.find(digit) == guess.find(guess_digit):
                    bulls += 1
                elif digit == guess_digit:
                    cows += 1
                else:
                    continue

        print "Bulls {} and {} cows".format(bulls, cows)

        return bulls == 4
