import random

def get_guess():
    valid = False
    guess = 0
    while valid == False:
        user_input = input("Enter your guess: ")
        if user_input.isdigit():
            guess = int(user_input)
            valid = True
        else:
            print("Invalid input. Please enter a whole number.")
    return guess

