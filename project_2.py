# project_2.py: druhy projekt do Engeto Online Python Akademie
# author: Patrik Perutka
# email: patrino19@seznam.cz
# discord: patrik_44080

import re
import random
import time

#user-defined functions
def verify_number(input):

    ''' 
    Checks if a number does not start with zero, uses unique digits
    and has exactly four digits. If true, returns True, else returns False.
    Used for checking both user input and in the 'generate_rand_num' function
    to validate that the random generated number also complies with the rules.
    '''

    if re.fullmatch(r"[1-9][0-9]{3}",input):
        return len(set(input)) == 4
    return False 

def generate_rand_num():

    '''
    Generates a random number for the user to guess.
    Loops through possible numbers until a generated number complies 
    with the rules which is then checked by the 'verify_number' function. 
    '''

    while True:
        rand_num = str(random.randint(1000, 9999))
        if verify_number(rand_num):
            return rand_num
        
def evaluate_user_guess(user_guess, gen_num):

    ''' 
    Takes the user's guess, compares it to the generated number and 
    returns the number of bulls (correct number, correct position) and 
    cows (correct number, incorrect position). 
    '''

    bulls = 0
    cows = 0
    for i in range(4):
        if user_guess[i] == gen_num[i]:
            bulls += 1
        elif user_guess[i] in gen_num:
            cows += 1
    return bulls, cows 

def decide_singular_or_plural(result):

    ''' 
    Takes a result, specifically the tuple returned by the 
    'evaluate_user_guess' function, and assigns a list containing 
    corresponding singular or plural words "bull/bulls" or
    "cow/cows" to use in the printed output.
    '''

    return [
        "bull" if result[0] == 1 else "bulls",
        "cow" if result[1] == 1 else "cows"
        ]

#game introduction
rules = ''' 
The goal of this game is to guess a randomly selected four-digit number.
This number does not start with a 0 and all four digits are unique.
When you make your guess, you find out the amount of bulls and cows.
Bull is a correct number in a correct position, cow is a correct
number, but in the wrong position. 
'''

#welcomes the user and gives an option to display the rules
first_choice = (input(
"Hello and welcome to Bulls and Cows!\n\
To see the rules of the game, type 0.\n\
To start playing straight away, press any key.\n\
>>> "))

if first_choice == "0":
    print(rules)

#outer loop to allow multiple runs of the program if the user wants to
while True:
    rand_num = generate_rand_num() 
    tries = 0

    #starts a timer
    start_time = time.time()

    print("-" * 45)
    print("Enter a number: ")

    #inner loop running until the user's guess is correct and counting valid tries
    while True:
       guess = input(">>> ")
       if verify_number(guess):
           tries += 1
           answer = evaluate_user_guess(guess, rand_num)
           output = decide_singular_or_plural(answer)
           if guess != rand_num:
               print(f"{answer[0]} {output[0]}, {answer[1]} {output[1]}")
               print("-" * 45)
           else:
               end_time = time.time() #ends the timer
               elapsed_time = end_time - start_time #counts elapsed time 
               print(f"Congratulations, you got it! It took you {tries} attempts and {round(elapsed_time/60, 1)} minutes. Good job!")
               break #breaks the inner loop after the number is guessed 
           
    if input("To play again, press 1. To exit, press any key.\n>>> ") != "1":
        break #breaks the outer loop if the user does not want to continue playing 