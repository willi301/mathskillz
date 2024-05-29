import random


def func1():
    print("testing")


# get difficulty
def getDifficulty():
    print("What level do you want the difficulty of the quiz?")
    diff = 0
    diff = input("Input 1 = easy, 2 = medium, 3 = hard: ")
    while 3 < int(diff) or int(diff) < 1:
        diff = input("Incorrect Input, please select 1, 2, or 3:")
    return diff

# make functions to ask questions
def questions(a, b, q):
    n1 = random.randrange(a, b, 3)
    n2 = random.randrange(a, b, 3)
    answer = input("Question. " + str(q) + " " + str(n1) + " + " + str(n2) + ": ")
    if(n1 + n2 == int(answer)):
        return 1
    else:
        return 0

# run game logic
def playGame(diff):
    total = 0
    question = 1
    #prompt question for easy mode
    if(diff == "1"):
        while question < 11:
            result = questions(1, 10, question) #ask the question
            question += 1                       #increment question number
            if(result == 1):
                total += 1                      #increment point
    #prompt question for medium mode
    elif(diff == "2"):
        while question < 11:
            result = questions(11, 99, question)
            question += 1
            if(result == 1):
                total += 1
    #prmopt question for hard mode
    elif(diff == "3"):
        while question < 11:
            result = questions(101, 999, question)
            question += 1
            if(result == 1):
                total += 1
    
    return total
