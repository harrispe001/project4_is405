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


    def add_row(row_number, input_string) :
        for i, letter in  enumerate(input_string) :
            gw.set_square_letter(row_number, i, letter) 


    # get random word from word list and make it an array
    correct_answer = random.choice(FIVE_LETTER_WORDS)
    correct_answer_list = list(correct_answer)


    gw = WordleGWindow()

    #temporary - adds random string to first row
    add_row(0, correct_answer)
    
    gw.add_enter_listener(enter_action)

    
# Startup code

if __name__ == "__main__":
   wordle()


