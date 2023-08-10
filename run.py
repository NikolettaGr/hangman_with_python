import random
import os
from words import easy_list, medium_list, hard_list

def clear_screen():
    """
    Clears the terminal screen based on
    the operating system type.
    """
    os.system("cls" if os.name == "nt" else "clear")

def welcome_message():
    """
    Displays the welcome message and menu options to
    the player.
    """
    print("Welcome to Hangman Game! 😀")
    print("Options:")
    print("1. Rules")
    print("2. Start Game")

    choice = input("Enter your choice (1 or 2): \n")

    if choice == "1":
        show_rules()
        print("1.Go back 🔙")
        answer = input("Enter number 1 to go back: \n")
        if answer == "1":
            clear_screen()
            welcome_message()

    elif choice == "2":
        main()
    else:
        print("Invalid choice. Please enter 1 or 2.")


def show_rules():
    """
    Displays the rules of the Hangman game.
    """
    print("""\nThe objective of Hangman is to guess a hidden word letter by letter.\n
The player has a limited number of attempts to guess the word correctly.\n
For each incorrect gues, a part of a 'hangman' figure is drawn.\n
The player wins by guessing the word before the hangman figure is fully drawn,\n
and loses if the 'hangman' figure is completed before guessing the word.\n""")


def main():
    """
    Main function that handles level selection
    and gameplay.
    """
    clear_screen()

    while True:
        print("Choose level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit")
    
        level_choice = input("Enter your choice (1, 2, 3, or 4 to exit): \n")

        if level_choice == "1":
            word_list = easy_list
        elif level_choice == "2":
            word_list = medium_list
        elif level_choice == "3":
            word_list = hard_list
        elif level_choice == "4":
            clear_screen()
            welcome_message()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

        word = get_word(word_list)
        play(word)   


def get_word(word_list):
    """
    Randomly selects a word from the given word lists.
    """
    return random.choice(word_list).upper()


def play(word):
    """
    Manages the game logic nad gameplay loop for guessing the word.
    """
    clear_screen()

    # Initialize game variables
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman! 🙌")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        #Get user's guess
        guess = input("Please guess a letter or word: ").upper()

        #Check if the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)

                # Update the word completion with correct guesses
                word_as_list = list(word_completion)
                indices = [index for index in range(len(word)) if word[index] == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        #Check if the guess is a full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

        # Display hangman state and word completion
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # Print game result
    if guessed:
        print("Congrats, you guessed the word! You win! 🎉")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + ". Maybe next time! 😔" )


def display_hangman(tries):
    """
    Displays the current state of the hangman figure
    based on remaining tries.
    """
    stages = [
        """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                """,

        """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
                """,

        """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
                """,

        """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
                """,

        """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                """,

        """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """,

        """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                """
    ] 
    return stages[tries]              


clear_screen()                
welcome_message()