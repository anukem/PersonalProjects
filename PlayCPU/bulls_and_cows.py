import random

def generate_secret():
    '''Generates a 4 digit number with no repaeat digits''
It converts the number to a string and returns it'''
#Create a list with all posible integers
    L = [0,1,2,3,4,5,6,7,8,9]
#Pop each number and concatenate each into secret
    firstInt = str(L.pop(random.randint(0, len(L)-1)))
    secondInt = str(L.pop(random.randint(0, len(L)-1)))
    thirdInt = str(L.pop(random.randint(0, len(L)-1)))
    fourthInt = str(L.pop(random.randint(0, len(L)-1)))

    secret = firstInt + secondInt + thirdInt + fourthInt
    return secret
def count_bulls(guess,answer):
    '''Returns the number of bulls the guess earns when the
secret number is answer'''
#Make bulls zero and have it incrememnt everytime it finds a number in the right place
    bulls = 0
    for i in range(0, 4):
        if guess[i] in answer and guess[i] == answer[i]:
            bulls = bulls + 1       
    return bulls
def repeatedNumberCheck(guess):
    itRepeats = False
    for i in guess:
        if guess.count(i) > 1:
            itRepeats = True
            return itRepeats
    return itRepeats
print(repeatedNumberCheck('1234'))


def count_cows(guess,answer):
    '''Returns the number of bulls the guess earns when the
secret number is answer'''
#have cows increment in the loop everytime it find a number in the word, but
#not in the right place
    cows = 0
    bulls = count_bulls(guess, answer)
    numberString = "1234567890"
    for i in range(0,4):
        if guess[i] in answer and guess[i] != answer[i]:
            cows = cows + 1
#Make sure special case is taken care of if they repeat digits
    if bulls >= 1:
       for i in numberString:
           if i in guess:
               x = guess.count(i)
               if x >= 2:
                   cows = 0
    elif bulls == 0:
        for i in numberString:
            if i in guess:
                x = guess.count(i)
                if x == 2:
                    cows = cows - 1
                elif x == 3:
                    cows = cows - 2

    return cows

