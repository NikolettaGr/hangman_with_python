import random
import os
import colorama
from colorama import Fore, Style
from words import *
import stages
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
    print(f"{Fore.MAGENTA}Welcome to Hangman Game! 😀{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Options:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1.{Style.RESET_ALL} Rules")
    print(f"{Fore.GREEN}2.{Style.RESET_ALL} Start Game")


    
    while True:
        choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): \n{Style.RESET_ALL}")
        if choice == "1":
            show_rules()
            print(f"{Fore.GREEN}1.{Style.RESET_ALL}Go back 🔙")
            answer = input(f"{Fore.YELLOW}Enter number 1 to go back: \n{Style.RESET_ALL}")
            if answer == "1":
                clear_screen()
                welcome_message()

        elif choice == "2":
            main()
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}")
            continue


def show_rules():
    """
    Displays the rules of the Hangman game.
    """
    print(f"""{Fore.GREEN}\nThe objective of Hangman is to guess a hidden word letter by letter.\n
The player has a limited number of attempts to guess the word correctly.\n
For each incorrect gues, a part of a 'hangman' figure is drawn.\n
The player wins by guessing the word before the hangman figure is fully drawn,\n
and loses if the 'hangman' figure is completed before guessing the word.\n{Style.RESET_ALL}""")


def main():
    """
    Main function that handles level selection
    and gameplay.
    """
    clear_screen()

    while True:
        print(f"{Fore.GREEN}Choose level:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1.{Style.RESET_ALL} Easy")
        print(f"{Fore.GREEN}2.{Style.RESET_ALL} Medium")
        print(f"{Fore.GREEN}3.{Style.RESET_ALL} Hard")
        print(f"{Fore.RED}4.{Style.RESET_ALL} Exit")
    
        level_choice = input(f"{Fore.YELLOW}Enter your choice (1, 2, 3, or 4 to exit): \n{Style.RESET_ALL}")

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
            print(f"{Fore.RED}Invalid choice. Please enter 1, 2, 3 or 4.{Style.RESET_ALL}")
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

    print(f"{Fore.MAGENTA}Let's play Hangman! 🙌{Style.RESET_ALL}")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        #Get user's guess
        guess = input(f"{Fore.YELLOW}Please guess a letter or word: {Style.RESET_ALL}").upper()

        #Check if the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{Fore.RED}You already guessed the letter {guess}.{Style.RESET_ALL}")
            elif guess not in word:
                print(f"{Fore.RED}{guess} is not in the word.{Style.RESET_ALL}")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{Fore.CYAN}Good job, {guess} is in the word!{Style.RESET_ALL}")
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
                print(f"{Fore.RED}You already guessed the word {guess}.{Style.RESET_ALL}")
            elif guess != word:
                print(f"{Fore.RED}{guess} is not in the word.{Style.RESET_ALL}")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(f"{Fore.RED}Not a valid guess.{Style.RESET_ALL}")

        # Display hangman state and word completion
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # Print game result
    if guessed:
        print(f"{Fore.GREEN}Congrats, you guessed the word! You win!{Style.RESET_ALL} 🎉")
    else:
        print(f"{Fore.RED}Sorry, you ran out of tries. The word was " +
              word + ". Maybe next time!😔" )
              

clear_screen()                
welcome_message()