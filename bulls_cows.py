import pdb
import random


def correct_number(user_number):
    return len(user_number) == 4 and user_number[0] != '0' and user_number.isdigit() and len(set(list(user_number))) == 4


def bulls_cows():
    computer_number = str(''.join(random.sample("0123456789", 4)))

    print "Computer number is {}".format(computer_number)
    user_number = raw_input('Enter a number between 1000 and 9999: ')

    while not correct_number(user_number):
        user_number = raw_input('Invalid guess. Try again: ')

    guesses = 1

    while user_number != computer_number:
        bulls = 0
        cows = 0

        for computer_digit in computer_number:
            for user_digit in user_number:
                if computer_digit == user_digit and computer_number.find(computer_digit) == user_number.find(user_digit):
                    bulls += 1
                elif computer_digit == user_digit:
                    cows += 1
                else:
                    continue
        guesses += 1

        print "You found: {} bulls and {} cows.".format(bulls, cows)
        user_number = raw_input('Try again with another guess: ')

        while not correct_number(user_number):
            user_number = raw_input('Invalid guess. Try again: ')

    print "You found the number {} by making {} correct guesses.".format(computer_number, guesses)


bulls_cows()
