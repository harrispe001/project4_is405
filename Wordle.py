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

        #Display winning message
        if input_string.lower() == correct_answer.lower() :
            for col in range(0, 5):
                gw.set_square_color(gw.get_current_row(), col, "#66BB66") 

            #Output winning message
            if gw.get_current_row() > 0 :
                gw.show_message(f'You Won! It took you {gw.get_current_row() + 1} tries')
            else :
                gw.show_message(f'You Won! It took you {gw.get_current_row() + 1} try')

        #Display yellows & greens for incorrect guess
        elif input_string.lower() in FIVE_LETTER_WORDS:
            gw.show_message("That is a word!")
            
            #Returns positions for greens returns positions for all chars not green
            green_positions, yellow_cands = check_for_green(input_string, correct_answer)

            #Returns which chars are yellow
            yellow_positions = check_for_yellow(input_string, correct_answer, yellow_cands)

            #set tiles to their proper color
            for pos in range(0, 5):
                if pos in green_positions:
                    gw.set_square_color(gw.get_current_row(), pos, "#66BB66")

                #make tile yellow  - unless key is already green
                elif pos in yellow_positions:
                    gw.set_square_color(gw.get_current_row(), pos, "#CCBB66")

            if gw.get_current_row()==5:
                gw.show_message(f'You did not guess it! The correct answer is: {correct_answer.upper()}' )
            else:
                gw.set_current_row(gw.get_current_row() + 1)

        #What to do with invalid word
        else:
            input_string = input_string.strip()
            if len(input_string) != 5:
                gw.show_message("Enter 5 letter word")
            else:
                gw.show_message(input_string + " not in word list" )



    def add_row(row_number, input_string) :
        for i, letter in  enumerate(input_string) :
            gw.set_square_letter(row_number, i, letter) 


    def set_answer() :
        return random.choice(FIVE_LETTER_WORDS)

    #Returns a list of green tiles and potential yellows
    def check_for_green(guess, answer) :
        green_pos = []
        yellow_candidates = []

        for n in range(0, 5):
            if guess.lower()[n] == answer[n]:
                green_pos.append(n)

            else:
                yellow_candidates.append(n)

        return green_pos, yellow_candidates


    #Recieves list of letters that aren't green. Checks to see if any remaining letters from guess match correct answer letters left
    def check_for_yellow(guess, answer, yellow_cands):
        yellow_pos = []
        answer_string_not_green_chars = []
        input_string_not_green_chars = []

        #list of letters left after removing greens
        for n in yellow_cands:
            answer_string_not_green_chars.append(answer[n])
            input_string_not_green_chars.append(guess.lower()[n])

        for i in yellow_cands:
            if guess.lower()[i] in answer_string_not_green_chars:
                yellow_pos.append(i)
                #only remove first value
                answer_string_not_green_chars.remove(guess.lower()[i])
        
        return yellow_pos


    
    #Set correct answer for wordle game
    #correct_answer = set_answer()
    correct_answer = set_answer()

    #Start window    
    gw = WordleGWindow()
    
    #temporary show the answer for testing
    gw.show_message(correct_answer)

    gw.add_enter_listener(enter_action)
    
    


    
# Startup code

if __name__ == "__main__":
   wordle()


