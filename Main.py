import random


# board: dictionary with lists
# 4 colors: 1,2,3,4, 0: null
# input management
# length of code is changeable


# randomly generate the initial code
def generate_code(length, blanks):
    global color
    code = []
    for c in range(length):
        if blanks == True:
            color = random.randrange(0, 7)
        else:
            color = random.randrange(1, 7)
    code.append(color)
    return code


def guess(code_length):
    temp_guess = []
    for g in range(code_length):
        guess = int(input("Enter your quest 1 by 1"))
        temp_guess.append(guess)
    return temp_guess


def compare(user_guess, code):
    # black peg: right color & position
    # white peg: right color, wrong position
    # blank: wrong color, doesn't appear
    # key pegs have no order
    index = 0
    compared_result = [t.append("Blank") for t in range(len(user_guess))]
    for g in range(len(user_guess)):
        if user_guess[index] == code[index]:
            compared_result.replace(random.randrange(0, len(code) + 1), "Black")
    return compared_result


def check_compared(compared_result):
    result = compared_result.count(compared_result[0]) == len(compared_result)
    if result == True:
        return "The codebreaker has won!"


def play():
    # game rules
    code_length = 4
    blanks = True
    code = generate_code(code_length, blanks)
    rounds = 8
    for r in range(rounds):
        user_guess = guess(code_length)
        compared_result = compare(user_guess, code)
        print("Compared result")
        print(check_compared(compared_result))
