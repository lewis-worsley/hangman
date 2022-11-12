import random
from words import words

class Color:
    """
    Sets colors to be called for different texts.
    """
    RESET = '\033[0m'
    RED = '\033[91m'

def opening_credits():
    global players_name
    
    players_name = input("Enter your name: ")
    print(f"Hi {players_name}, let's play!")


def play_game(word):
    """
    To initate the start of the game for the user to begin playing
    """



def select_word():
    """
    Generates a random word from the words.py file. The player must guest
    this word. A new word is selected after each round.
    """
    random_word = random.choice(words).upper()
    return random_word

def graphics(image_of_lives):
    display_image = [
        f"""
              =======
              |/    |
              |     {Color.RED}O{Color.RESET}
              |    /|\\
              |     |
              |    / \\
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     0
              |    /|\\
              |     |
              |    /
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     0
              |    /|\\
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     0
              |    /|
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     0
              |     |
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        f"""
              =======
              |/    |
              |     0
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """
    ]

    return display_image[image_of_lives]

def main():
    """
    To run the game and present the opening credits to the user
    """
    opening_credits()
    select_word()
    play_game(select_word())

print(
        """
                
__    __                                                                 
|  \  |  \                                                                
| $$  | $$  ______   _______    ______   ______ ____    ______   _______  
| $$__| $$ |      \ |       \  /      \ |      \    \  |      \ |       \ 
| $$    $$  \$$$$$$\| $$$$$$$\|  $$$$$$\| $$$$$$\$$$$\  \$$$$$$\| $$$$$$$\
| $$$$$$$$ /      $$| $$  | $$| $$  | $$| $$ | $$ | $$ /      $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$| $$__| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$
| $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$ | $$ | $$ \$$    $$| $$  | $$
\$$   \$$  \$$$$$$$ \$$   \$$ _\$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$   \$$
                              |  \__| $$                                  
                              \$$    $$                                  
                               \$$$$$$                                   
        
        """
                
    )

print("Welcome to Hangman!")

main()