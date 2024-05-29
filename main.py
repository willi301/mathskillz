
from cProfile import label
import os
import sys
from tkinter import ttk
from module import *
import tkinter
from tkinter import *


# function to get event selector
def on_select(event):
    selected_item = ttk.Combobox.get()
    label.config(text="Select difficulty: " + selected_item)


# Gui loop
root = tkinter.Tk()
root.geometry("500x300")
root.title("MathSkillz")
w = tkinter.Label(root, text="Welcome to MathSkillz")
w.pack()
w = tkinter.Label(root, text="The application to test your math skills")
w.pack()


# choose difficulty frmae
difficulty = Frame(root)
difficulty.pack(pady=(20,0))

# label
w2 = tkinter.Label(difficulty, text="Select Difficult: ")
w2.pack(side = LEFT, expand = True, fill = BOTH)

# combo box
combo_box = ttk.Combobox(difficulty, values=["Easy", "Medium", "Hard"])
combo_box.pack(side = LEFT, expand = True, fill = BOTH)

combo_box.set("Choose")


# enter button
b = Button(root, text="enter", width=30)
b.pack(side= BOTTOM, pady=(0, 50))


root.mainloop()




# #functionality is being turned off at the moment

# # welcome user to program
# print("Hello, World")

# #get input from user
# diff = 0
# diff = getDifficulty()
# # get difficulty
# match diff:
#     case 1:
#         print("You choose: easy")
#     case 2:
#         print("You choose: medium")
#     case 3:
#         print("You choose: hard")

# # run game logic
# point = playGame(diff)
# print("You got : " + str(point) + " points")

