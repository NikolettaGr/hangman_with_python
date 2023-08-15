import random
import os
import colorama
from words import *
from stages import display_hangman

colorama.init(autoreset=True)


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
    print(f"{colorama.Fore.MAGENTA}Welcome to Hangman Game! 😀")
    print(f"{colorama.Fore.GREEN}Options:{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.GREEN}1.{colorama.Style.RESET_ALL} Rules")
    print(f"{colorama.Fore.GREEN}2.{colorama.Style.RESET_ALL} Start Game")

    while True:
        choice = input(f"{colorama.Fore.YELLOW}Enter your choice (1 or 2): \n")
        if choice == "1":
            show_rules()
            wait_for_any_key()
            
            
        elif choice == "2":
            main()
        else:
            print(f"{colorama.Fore.RED}Invalid choice. Please enter 1 or 2.")
            continue


def wait_for_any_key():
    print(f"{colorama.Fore.YELLOW}Press any key to go back...")
    input()  # Wait for any key press
    welcome_message()


def show_rules():
    """
    Displays the rules of the Hangman game.
    """
    print(f"""{colorama.Fore.GREEN}
The objective of Hangman is to guess a hidden word letter by letter.\n
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
        print(f"{colorama.Fore.GREEN}Choose level:")
        print(f"{colorama.Fore.GREEN}1.{colorama.Style.RESET_ALL} Easy")
        print(f"{colorama.Fore.GREEN}2.{colorama.Style.RESET_ALL} Medium")
        print(f"{colorama.Fore.GREEN}3.{colorama.Style.RESET_ALL} Hard")
        print(f"{colorama.Fore.RED}4. Exit{colorama.Style.RESET_ALL}")

        level_choice = input(f"""{colorama.Fore.YELLOW}
Enter your choice (1, 2, 3, or 4 to exit): \n""")

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
            print(f"""{colorama.Fore.RED}
Invalid choice. Please enter 1, 2, 3 or 4.""")
            continue

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

    print(f"{colorama.Fore.MAGENTA}Let's play Hangman! 🙌")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        # Get user's guess
        guess = input(
            f"{colorama.Fore.YELLOW}Please guess a letter or word: ").upper()

        # Check if the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"""{colorama.Fore.RED}
You already guessed the letter {guess}.""")
            elif guess not in word:
                print(f"{colorama.Fore.RED}{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{colorama.Fore.CYAN}Good job, {guess} is in the word!")
                guessed_letters.append(guess)

                # Update the word completion with correct guesses
                word_as_list = list(word_completion)
                indices = [index for index in range(
                    len(word)) if word[index] == guess]

                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        # Check if the guess is a full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"""{colorama.Fore.RED}
You already guessed the word {guess}.""")
            elif guess != word:
                print(f"{colorama.Fore.RED}{guess} is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(f"{colorama.Fore.RED}Not a valid guess.")

        # Display hangman state and word completion
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # Print game result
    if guessed:
        print(f"""{colorama.Fore.GREEN}
Congrats, you guessed the word! You win! 🎉""")
        print("-----------------------------------------")
    else:
        print(f"{colorama.Fore.RED}Sorry, you ran out of tries. The word was " +
word + ". Maybe next time!😔")
        print("------------------------------------------")


def call():
    clear_screen()
    welcome_message()


call()

