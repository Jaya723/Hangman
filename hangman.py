import random
import string
from words_file import words  

# Function to get a valid word for Hangman (no hyphens or spaces)
def get_valid_word(words):
    word = random.choice(words).upper()  # Ensure the word is in uppercase
    # Skip words with invalid characters like hyphens or spaces
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

# Main Hangman game function
def hangman():
    word = get_valid_word(words)  # Select a valid word
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # All uppercase English letters (A-Z)
    used_letters = set()  # Track letters guessed by the user

    lives = 6  # Number of incorrect guesses allowed

    # Game loop continues until the user has guessed all letters or runs out of lives
    while len(word_letters) > 0 and lives > 0:
        # Display the letters the user has guessed so far
        print("\nYou have used these letters: ", ' '.join(sorted(used_letters)))
        
        # Display the current state of the word (e.g., W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        # Display remaining lives
        print(f"Lives remaining: {lives}")
        
        # Get user input
        user_letter = input("Guess a letter: ").upper()

        # Check if the input is a valid guess
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add the letter to the set of used letters

            # Check if the guessed letter is in the word
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove the letter from the word letters set
                print(f"Good job! {user_letter} is in the word.")
            else:
                lives -= 1  # Deduct a life for incorrect guess
                print(f"Oops! {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("You have already guessed this letter! Try again.")
        else:
            print("Invalid input! Please enter a valid letter.")

    # Game over conditions
    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Start the game
hangman()



