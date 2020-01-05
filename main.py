"""Guess the Number - Python Learning

Write a programme where the computer randomly generates a number between 0 and 20.
The user needs to guess what the number is. If the user guesses wrong, tell them 
their guess is either too high, or too low. This will get you started with the 
random library if you haven't already used it. 

From https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs


"""

import random

print("Type your username.")

str_username = input()

correct_response_username =  "Hi {}, welcome to the Guess Your Number Game. Start typing a number between 1 and 20.".format(str_username)

print(correct_response_username)

def game_logic():
    bool_correct_number = False
    int_correct_number = random.randint(1,20)
    int_turn_counter = 0
    while bool_correct_number is not True:
        int_user_input = int(input())
        int_turn_counter += 1

        if int_user_input > int_correct_number:
            print("{} is too high!".format(int_user_input))
        
        elif int_user_input < int_correct_number:
            print("{} is too low!".format(int_user_input))

        else:
            print("Hooray! {} was the correct guess! You guessed this in {} turns.".format(int_correct_number, int_turn_counter))
            break


game_logic()

## Not Yet refactored.