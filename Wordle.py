# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message(correct_answer_list)


    def add_row() :
        for i, letter in  enumerate(correct_answer_list) :
            gw.set_square_letter(0, i, letter) 

    correct_answer = random.choice(FIVE_LETTER_WORDS)
    correct_answer_list = list(correct_answer)

    gw = WordleGWindow()
    add_row()
    gw.add_enter_listener(enter_action)

    
# Startup code

if __name__ == "__main__":
   wordle()


