from player import Player


class Human(Player):

    """Return boolean if the player number is valid
    """

    def correct_number(self, number):
        return len(number) == 4 and number[0] != '0' and number.isdigit() and len(set(list(number))) == 4

    """Set the human number to instance variable
    """

    def ask_for_number(self):
        self.number = self.ask('Enter your number: ')

    """Return the guess of the player(human)
    """

    def ask(self, prompt):
        guess = raw_input(prompt)

        while not self.correct_number(guess):
            guess = raw_input('Invalid number. Try again: ')

        return guess

    """Return boolean if the human has won or not
    """

    def play_turn(self, number):
        guess = self.ask('Enter your guess number: ')

        if self.bulls_and_cows(number, guess):
            print "You have won!"

            return True
        else:
            return False

    """Return name of the human
    """

    def player_name(self):
        return "You"
