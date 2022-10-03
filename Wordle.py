# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    # Checks if input is in word list and displays messages
    def enter_action(input_string):

        #What to do on correct Answer
        if input_string.lower() == correct_answer.lower() :
            for col in range(0, 5):
                gw.set_square_color(gw.get_current_row(), col, "#66BB66") 
            gw.show_message(f'You Won! It took you {gw.get_current_row() + 1} trie(s)')

        #what to do if enter valid word
        elif input_string.lower() in FIVE_LETTER_WORDS:
            gw.show_message("That is a word!")
            gw.set_current_row(gw.get_current_row() + 1)

        #What to do with invalid word
        else:
            gw.show_message(input_string + " not in word list")



    def add_row(row_number, input_string) :
        for i, letter in  enumerate(input_string) :
            gw.set_square_letter(row_number, i, letter) 


    def set_answer() :
        return random.choice(FIVE_LETTER_WORDS)



    # get random word from word list and make it an array


    correct_answer = set_answer()
    #correct_answer_list = list(correct_answer)
    correct_guess = False


    
    gw = WordleGWindow()
    
        #temporary
    gw.show_message(correct_answer)

    gw.add_enter_listener(enter_action)
    
    


    
# Startup code

if __name__ == "__main__":
   wordle()


