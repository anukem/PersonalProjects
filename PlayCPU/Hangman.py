# *********************
# Hangman Test Code
# 22 July 2015
# *********************

import random

# *********************************************************************************************************************************************************** #

# Word Banks [easy_0, medium_1, hard_2]
easy = {"food": ["apple", "banana", "chicken", "orange", "caviar", "macaroon", "wasabi"], "sports": ["football", "windsurfing"]}
medium = {"food": ["guacomole", "hazelnut", "walnut", "coconut", "cauliflower", "carbohydrate", "alfalfa"], "sports": ["pentathlon", "aerobics", "gymnasium", "skateboarding", "unicycle"]}
hard = {"food": ["sauerkraut", "zucchini", "licorice", "calimari"], "sports": ["parasailing", "olympics", "zorbing", "parkour", "snorkelling", "quidditch"]}

word_banks = [easy , medium, hard]
# *********************************************************************************************************************************************************** #

def generate_menu():
    """Creates menu of options for game"""
    print("Welcome to Hangman!")
    print("Please select a difficulty below:\n")
    print("* Easy\n* Medium\n* Hard\n")

generate_menu()
choice = input().lower()
if choice == "easy":
    lvl = 0
elif choice == "medium":
    lvl = 1
elif choice == "hard":
    lvl = 2
while (choice != 'easy') and (choice != 'medium') and (choice != 'hard'):
    choice = input("Oops, wrong input, try again ")
    if choice == "easy":
        lvl = 0
        break
    elif choice == "medium":
        lvl = 1
        break
    elif choice == "hard":
        lvl = 2
        break

#choice of word category
random_num = random.randint(0, 1)

if random_num == 0:
    category = "food"
elif random_num == 1:
    category = "sports"

# choice of word itself
index = random.randint(0, len(word_banks[lvl][category])-1)
word = word_banks[lvl][category][index]

# *********************************************************************************************************************************************************** #

def draw_noose(limbs):
    """noose_img = "  ________\n  |/\t\t |\n  |\n  |\n /|\\\n/ | \\" """
    line1 = "  ________"
    line2 = "  |/\t|"
    line3 = "  |"
    head = "  |     O"
    line4 = "  |"
    body = "  |     |"
    l_arm = "  |    /|"
    r_arm = "  |    /|\\ "
    line5 = " /|\\"
    l_leg = " /|\\    /"
    r_leg = " /|\\    /\\"
    line6 = "/ | \\"

    if limbs == 0:
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        print(line6)
    elif limbs == 1:
        print(line1)
        print(line2)
        print(head)
        print(line4)
        print(line5)
        print(line6)
    elif limbs == 2:
        print(line1)
        print(line2)
        print(head)
        print(body)
        print(line5)
        print(line6)
    elif limbs == 3:
        print(line1)
        print(line2)
        print(head)
        print(l_arm)
        print(line5)
        print(line6)
    elif limbs == 4:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(line5)
        print(line6)
    elif limbs == 5:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(l_leg)
        print(line6)
    elif limbs == 6:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(r_leg)
# *********************************************************************************************************************************************************** #
def game(word):

    # game letters in list
    correct = list(word)
    # print blanks
    answer = [("_") for letter in correct]
    print(" ".join(answer))

    limbs = 0
    wrong = []
    correct_letter = 0
    hanged = False
    hint = False
    chance = ''
    while hanged == False:
        # user guess letter
        guess = str(input('What letter would you like to guess? ')).lower()
        for i in range(0, len(correct)):
            if guess == correct[i]:
                correct_letter += 1
                answer[i] = guess
        if guess not in correct and guess not in wrong:
            wrong.append(guess)
            limbs += 1
            draw_noose(limbs)
        if (limbs == 3 or limbs == 4) and hint == False:
            chance = input("Would you like a hint? (y/n) ").lower()
        if chance == 'yes' or chance == 'y':
            hint = True
            print("The category is " + category)
        print(" ".join(answer))
        print(wrong)
        if len(correct) == correct_letter:
            hanged = True
        if len(wrong) == 6:
            hanged = True
            print('Better luck next time! ')
game(word)

retry = input("Would you like to play again? (y/n) ").lower()
while retry == 'y':
    generate_menu()
    choice = input().lower()
    if choice == "easy":
        lvl = 0
    elif choice == "medium":
        lvl = 1
    elif choice == "hard":
        lvl = 2
    while (choice != 'easy') and (choice != 'medium') and (choice != 'hard'):
        choice = input("Oops, wrong input, try again ")
        if choice == "easy":
            lvl = 0
            break
        elif choice == "medium":
            lvl = 1
            break
        elif choice == "hard":
            lvl = 2
            break

    #choice of word category
    random_num = random.randint(0, 1)

    if random_num == 0:
        category = "food"
    elif random_num == 1:
        category = "sports"

    # choice of word itself
    index = random.randint(0, len(word_banks[lvl][category])-1)
    word = word_banks[lvl][category][index]
    game(word)
    retry = input("Would you like to play again? (y/n) ").lower()
