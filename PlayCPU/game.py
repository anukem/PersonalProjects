import bulls_and_cows as bc

def main():
# Do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')

def play_game():
    '''Plays one interactive game of bulls and cows on the console'''
    answer = bc.generate_secret()
    guess = input("What would you like to guess? ")
    while (len(guess) != 4) or bc.repeatedNumberCheck(guess) == True:
        guess = input("Oops try again! ")
    bulls = 0
    #Use a counter to keep track of the round
    counter = 1
    #Loop till they get the number right 
    while bc.count_bulls(guess, answer) < 4:
        print("You have " + str(bc.count_cows(guess, answer)) + " cow(s)")
        print("You have " + str(bc.count_bulls(guess, answer)) + " bull(s)") 
        guess = input("Try again? ")
        while(len(guess) != 4):
            guess = input("Four numbers only. ")
        counter = counter + 1
        print("Round: " + str(counter))
    print("You win! It took " + str(counter) + " turns")
       

main()

