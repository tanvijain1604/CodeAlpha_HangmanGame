# CodeAlpha_HangmanGame
Project Overview

This project is a simple text-based Hangman Game written in Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time before running out of chances.

Features
Randomly selects a word from a list of 5 predefined words.
Allows the player to guess one letter at a time.
Displays correctly guessed letters and hides unguessed letters.
Limits incorrect guesses to 6 attempts.
Detects win and loss conditions.
Prevents duplicate guesses.
Validates user input.
Technologies Used
Python 3
random module
Lists
Strings
while loop
if-else statements
How the Game Works
The program randomly selects a word.
The player enters a letter.
If the letter exists in the word:
The letter is revealed.
If the letter does not exist:
The number of incorrect guesses increases.
The game continues until:
The player guesses the entire word (Win), or
The player reaches 6 incorrect guesses (Lose).
Algorithm
Import the random module.
Create a list of predefined words.
Randomly select a word from the list.
Initialize:
guessed_letters
incorrect_guesses
max_guesses
Start a while loop.
Display the current state of the word.
Check if the word is fully guessed.
Ask the player for a letter.
Validate the input.
Check whether the guessed letter is in the word.
Update game status accordingly.
Repeat until the player wins or loses.
Display the final result.
