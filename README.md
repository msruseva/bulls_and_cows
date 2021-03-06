# Bulls and Cows

Bulls and cows is an old code-breaking mind or paper and pencil game for two players. The main idea of the game is to guess the number of the opponent, in this case the computer's number. The first player who guesses the number of his opponent wins the game. After the end of the game you can choose to play another game. If you type 'y' the opponent that had lost the previous game will have the change to give his guess first.

## Installation

Download the game by entering the following command:

```
https://github.com/msruseva/bulls_and_cows
```

You need to have `python` 2.7 installed in order to play the game.

## Starting the game

Enter the following command to start the game:

```
$ python game.py
```

This will open an interactive shell where you can play the game against a computer AI.

## Example game

```
$ Enter you number: 1234
$ Computer number is: 9453
$ Enter your guess number: 9845
$ You found 1 bulls and 2 cows
$ Computer guess number is: 2365
$ Computer found 0 bulls and 1 cows
$ Enter your guess number: 12
$ Invalid number. Try again: 0123
$ Invalid number. Try again: 1223
$ Invalid number. Try again: 12bg
$ Invalid number. Try again: 9845
$ You found 4 bulls and 0 cows
$ You have won!
$ Play another game? Enter 'y' for yes: no
$ Bye ^_^
```
