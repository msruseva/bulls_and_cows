from human import Human
from computer import Computer
from player import Player


class Game:

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    """Run the game and return message after the end of the game

    The two options for the player after the end of the game is
    to start another or to quit the game.
    """

    def play(self):
        self.first_player.ask_for_number()
        self.second_player.ask_for_number()

        winner = None
        loser = None

        while winner == None:
            if self.first_player.play_turn(self.second_player.number):
                winner = self.first_player
                loser = self.second_player

            if winner == None:
                if self.second_player.play_turn(self.first_player.number):
                    winner = self.second_player
                    loser = self.first_player

        play_again = raw_input("Play another game? Enter 'y' for yes: ")

        if play_again == 'y':
            loser.reset()
            winner.reset()

            Game(loser, winner).play()
        else:
            print "Bye ^_^"

Game(Human(), Computer()).play()
