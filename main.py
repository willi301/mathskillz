
import os
import sys
from module import *

# welcome user to program
print("Welcome to MathSkillz")

#get input from user
diff = 0
diff = getDifficulty()
# get difficulty
match diff:
    case 1:
        print("You choose: easy")
    case 2:
        print("You choose: medium")
    case 3:
        print("You choose: hard")

# run game logic
point = playGame(diff)
print("You got : " + str(point) + " points")


