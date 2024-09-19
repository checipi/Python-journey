LOGO = """
   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       
"""

import random
import os
from time import sleep


EASY_GAME = 10
HARD_GAME = 5


def low_high(n1, n2):
    """Takes 2 numbers and checks which one is bigger or smaller 
    and returns 1"""
    if n1 > n2:
        print("Too High!")
    if n1 < n2:
        print("Too Low!")
    return 1
   

def difficulty():
    """Sets the difficulty of the game , 5 of 10 turns"""
    difficulty_choice = input("Choose a difficulty. Type \"easy\" or \"hard\": ")
    if difficulty_choice == "easy":
        return EASY_GAME
    else:
        return HARD_GAME
    
def end_game(user_input, random_no, tries):
    if tries == 0:
        print("You lose!")
        return False 
    if user_input == random_no:
        print("You win!")
        return False 


def number_guessing():
    """Number Guessing Game, guess a number between 1 and 100.
    The game has two diffcuilties: easy and hard"""
    continue_game = True 
    tries = 0
    random_no = random.choice(range(1, 101))
    

    print(LOGO,"\n" * 2)
    print("Welcome to the Number Guessing Game!\n\n")
    sleep(0.8)
    print("I'm thinking of a number between 1 an 100.")
    print(f"Random number: {random_no}\n\n")
    sleep(0.8)

   
    tries = difficulty()
   
    while continue_game:
        print(f"You have {tries} tries left.")
        user_input = int(input("Make a choice: "))
            
        tries -= int(low_high(user_input, random_no,))
        print(f"Tries: {tries}")
        continue_game = end_game(user_input, random_no, tries)
        
        # if tries == 0:
        #    print("You lose!")
        #    continue_game =  False 
        # if user_input == random_no:
        #    print("You win!")
        #    continue_game = False 
    choice = input("Wanna play again? \"yes\" or \"no\"  ")
    if choice == "yes":
        os.system('clear')
        number_guessing()
    
    
number_guessing()

