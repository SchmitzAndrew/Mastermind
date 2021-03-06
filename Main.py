import random

#board: dictionary with lists
#4 colors: 1,2,3,4, 0: null
#input management
#length of code is changeable


#gamerules
code_length = 4
blanks = True
guesses = 3

#randomly generate the initial code
code = []
for c in range(code_length):
    if blanks == True:
        color = random.randrange(0, 7)
    else:
        color = random.randrange(1,7)
    code.append(color)

def guess(code_length):
    temp_guess = []
    for g in range(code_length):
        guess = int(input("Enter your quest 1 by 1"))
        temp_guess.append(guess)
    return temp_guess

def play():
    pass
