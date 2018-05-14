import pdb
from human import Human
from computer import Computer
from player import Player

class Game:

    def __init__(self):
        self.user_player = Human()
        self.computer_player = Computer()
        self.current_player = self.user_player

    def play(self):
        number = self.user_player.ask_for_number()

        while True:
            guess = self.current_player.make_a_guess()

            if Player().bulls_and_cows(self.computer_player.number, guess):
                break
            else:
                self.change_player()

    def change_player(self):
        if self.current_player == self.user_player:
            self.current_player = self.computer_player
        else:
            self.current_player = self.user_player

Game().play()
