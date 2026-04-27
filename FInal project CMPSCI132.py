import random

# Number Guessing Game
# The computer picks a random number between 1 and 100.
# The player guesses until they get it right, with hints after each guess.
# The game tracks all guesses and lets the player replay.

def get_guess():
    # Prompt the player for a valid integer guess
    # Rejects non-numeric input and duplicate guesses
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

