import pdb
import random 
import string

def bulls_cows(computer_number, user_number):
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
		
		print "You found: " + str(bulls) + " bulls and " + str(cows) + " cows."
		user_number = str(input('Try again with another guess.'))

	return "You found the number {} by making {} guesses.".format(int(computer_number), guesses)
 
random_number = str(''.join(random.sample("0123456789", 4)))
print(random_number)
guess_number = str(input('Enter a number between 1000 and 9999: '))

print(bulls_cows(random_number, guess_number))