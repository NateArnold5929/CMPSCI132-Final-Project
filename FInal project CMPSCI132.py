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

def play_game():
    # Runs one full round of the guessing game
    secret_number = random.randint(1, 100)
    attempts = 0
    correct = False
    previous_guesses = []  # list to track all guesses this round

    print("\nI've picked a number between 1 and 100. Can you guess it?\n")

    while correct == False:
        guess = get_guess(previous_guesses)
        attempts += 1
        previous_guesses.append(guess)

        if guess < secret_number:
            print(f"Too low! Try a higher number.\n")
        elif guess > secret_number:
            print(f"Too high! Try a lower number.\n")
        else:
            correct = True
            print(f"\nCongratulations! You guessed it!")
            print(f"The number was {secret_number}.")
            print(f"Your guesses: {previous_guesses}")
            print(f"It took you {attempts} attempts.")
