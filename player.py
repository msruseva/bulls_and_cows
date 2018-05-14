class Player:

    """Returns true or false

    If the player has found the number of the other player returns true
    otherwise returns false
    """

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

        print "{} found {} bulls and {} cows".format(self.player_name(), bulls, cows)

        return bulls == 4

    """Return the name of the player
    """

    def player_name(self):
        return "Unknown"

    """Reset the number of the player
    """

    def reset(self):
        self.number = None
