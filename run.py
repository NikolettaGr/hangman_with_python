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

clear_screen()                
welcome_message()