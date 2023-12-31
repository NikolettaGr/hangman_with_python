Return back to the [README.md](README.md) file.

## Testing

The program was tested constantly during its development process.
Other users also tested it in order to spot possible grammatical mistakes that the code may present.

### Validators

Heroku's online validator [online validation tool](https://pep8ci.herokuapp.com/) was used to ensure that all of the project's Python source code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). 
This checking was done manually by copying python code and pasting it into the validator.

- **run.py**

![Python Validator](documentation/pep8-run.py.png)

- **words.py**

![Python Validator](documentation/pep8-word-list.png)

- **stages.py** - The PEP8 validator is highlighting numerous whitespace issues, but I'm hesitant to remove them, as doing so could disrupt the positioning of the hangman figures and potentially cause the game to malfunction.

![Python Validator](documentation/pep8-stages.png)



### Manually testing

 1. Run the code in your Python environment.
 2. The game will start with a welcome message and menu options.
 3. Choose option 1 to see the rules of the game.
 4. Press 1 again to go back to the main menu.
 5. Choose option 2 to start the game.
 6. Select a level (1 for Easy, 2 for Medium, 3 for Hard, 4 to Exit).
 7. If you choose a level, the game will randomly select a word from the chosen level's word list and display the initial hangman state and word completion.
 8. Enter a letter or word guess based on the displayed information.
 9. Continue guessing until you either correctly guess the word or run out of tries.
 10. After the game ends (either in a win or a loss), you'll see the result and the option to play again.