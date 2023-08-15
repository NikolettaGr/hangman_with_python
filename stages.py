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

