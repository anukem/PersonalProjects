import os
def OpeningMenu():
	print("Welcome to PlayCPU!")
	print("Please select a game to play")
	print('****************')
	print('* 1. Rock, Paper, Scissors')
	print('* 2. Hangman')
	print('* 3. Bulls and Cows')
	print('******************')
	return
OpeningMenu()
answer = 'yes'
while answer == 'yes' or answer == 'y':
	userInput = input("Enter a number (1,2,3) ")
	while (userInput != '1') and (userInput != '2') and (userInput != '3'):
			userInput = input("Please enter a number (1,2,3) ")
	userInput = int(userInput)
	if userInput == 1:
		#Play Rock, Paper, Scissors
		os.system('java RockPaperScissors')
	answer = input('Do you want to something else? (yes/no) (y/n) ')

