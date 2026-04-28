# Number Guessing Game

A terminal-based number guessing game written in Python. The computer generates a random number between 1 and 100 and the player tries to guess it. After each guess, the program gives feedback to help the player narrow it down.

## How to Run

1. Make sure Python is installed on your computer
2. Open a terminal and navigate to the folder containing the file
3. Run the following command: python number_guessing_game.py

## How to Play

- The computer picks a random number between 1 and 100
- Type your guess and press Enter
- The game will tell you if your guess is too high or too low
- Keep guessing until you get it right
- At the end you will see all your guesses and how many attempts it took
- You can choose to play again or quit

## Project Description

This is a final project for CMPSC 132 at Penn State University. The program is organized into three functions:

- get_guess(previous_guesses) handles user input, validates that it is numeric, and prevents duplicate guesses
- play_game() runs a single round of the game, tracks guesses in a list, and displays results when the player wins
- main() controls the overall flow and handles the replay prompt between rounds

## Features

- Random number generation between 1 and 100
- Input validation (rejects non-numeric input and duplicate guesses)
- Feedback after every guess (too high / too low)
- Tracks and displays all guesses made each round
- Replay option after each game
