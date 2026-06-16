import random

# List of predefined words
words = ["apple", "banana", "orange", "grape", "mango"]

# Choose a random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")
        print("Remaining guesses:", max_guesses - incorrect_guesses)

# Lose condition
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)