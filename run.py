import random
import os
from words import easy_list, medium_list, hard_list

def clear_screen():
    """
    Clears the terminal screen based on
    the operating system type.
    """
    os.system("cls" if os.name == "nt" else "clear")
