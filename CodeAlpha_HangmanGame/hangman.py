
import random


def display_word(secret_word, guessed_letters):
    """Display guessed letters and underscores for hidden letters."""
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word


def play_game():
    """Run one round of the Hangman game."""

    words = ["python", "developer", "computer", "programming", "keyboard"]

    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\n" + "=" * 40)
    print("          WELCOME TO HANGMAN!")
    print("=" * 40)

    while incorrect_guesses < max_attempts:

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}")

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            print("YOU WIN!")
            return

        # Get the player's guess
        guess = input("\nGuess a letter: ").lower().strip()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check whether the guess is correct
        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    # Display the final result if attempts run out
    print("\n" + "=" * 40)
    print("GAME OVER!")
    print("The correct word was:", secret_word)
    print("Better luck next time!")
    print("=" * 40)


def main():
    """Control the game and handle replay options."""

    while True:
        play_game()

        while True:
            replay = input("\nWould you like to play again? (yes/no): ").lower().strip()

            if replay in ["yes", "y"]:
                break
            elif replay in ["no", "n"]:
                print("\nThanks for playing Hangman. Goodbye!")
                return
            else:
                print("Invalid choice. Please enter yes or no.")


# Start the game
if __name__ == "__main__":
    main()
