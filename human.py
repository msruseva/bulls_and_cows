from player import Player


class Human(Player):

    def correct_number(self, number):
        return len(number) == 4 and number[0] != '0' and number.isdigit() and len(set(list(number))) == 4

    def ask_for_number(self):
        return self.ask('Enter your number: ')

    def make_a_guess(self):
        return self.ask('Enter your guess number: ')

    def ask(self, prompt):
        user_guess = raw_input(prompt)

        while not self.correct_number(user_guess):
            user_guess = raw_input('Invalid number. Try again: ')

        return user_guess
