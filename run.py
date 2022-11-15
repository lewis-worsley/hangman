import random
from words import words

class Color:
    """
    Sets colors to be called for different texts.
    """
    RESET = '\033[0m'
    RED = '\033[91m'

def opening_credits():
    global player_name
    
    player_name = input("Enter your name: ")
    print(f"Hi {player_name}, let's play!\n")


def play_game(word):
    """
    To initate the start of the game for the user to begin playing
    """

    print(word)

    guessed_letters = []
    lives = 6
    won = False
    chosen_word = "_" * len(word)
    print(chosen_word)

    while lives > 0 and not won:
        print(graphics(lives))
        print(chosen_word, "\n")
        guess_letter = input(("Please choose a letter: ")).upper()
        
        if guess_letter.isalpha() and len(guess_letter) == 1:
            if guess_letter not in guessed_letters:
                if guess_letter in word:
                    guessed_letters.append(guess_letter)
                    broken_word = list(chosen_word)
                    print(guessed_letters, "\n")
                    indices = [i for i, letter in enumerate(word)
                                if letter == guess_letter]
                    for index in indices:
                        broken_word[index] = guess_letter
                    chosen_word = "".join(broken_word)
                    
                    if "_" not in chosen_word:
                        won = True
                        print(chosen_word)
                        print(f"Congratulations {player_name}, you won!\n")
                        restart_game()

                else:
                    guessed_letters.append(guess_letter)
                    lives = lives - 1
                    print(f"{lives} lives left")
                    print(guessed_letters)
        
            elif guess_letter in guessed_letters:
                print(f"You've already guessed '{guess_letter}'. Choose a different letter. Here are your current guesses {guessed_letters}.\n")

        else:
            print(f"\nPlease select only one (1) letter. You selected '{guess_letter}' which contains {len(guess_letter)} letters.")
    
    if lives == 0:
        print(graphics(0))
        print(f"Game Over. You lose {player_name}! The correct word was {word}")
        restart_game()

def restart_game():
    """
    Provides the player with an opportunity to restart the game
    """

    player_restart = False

    while player_restart is False:

        player_response = input("\nAnother round of Hangman? (Y/N): ").upper()

        try:
            if player_response == "Y":
                new_word = select_word()
                play_game(new_word)
            
            elif player_response == "N":
                player_restart = True

                print(f"Until next time {player_name}...")
                
                print(
                    """
    
  ______                             __  __                            __ 
 /      \                           |  \|  \                          |  \
|  $$$$$$\  ______    ______    ____| $$| $$____   __    __   ______  | $$
| $$ __\$$ /      \  /      \  /      $$| $$    \ |  \  |  \ /      \ | $$
| $$|    \|  $$$$$$\|  $$$$$$\|  $$$$$$$| $$$$$$$\| $$  | $$|  $$$$$$\| $$
| $$ \$$$$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$    $$ \$$
| $$__| $$| $$__/ $$| $$__/ $$| $$__| $$| $$__/ $$| $$__/ $$| $$$$$$$$ __ 
 \$$    $$ \$$    $$ \$$    $$ \$$    $$| $$    $$ \$$    $$ \$$     \|  \
  \$$$$$$   \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  _\$$$$$$$  \$$$$$$$ \$$
                                                  |  \__| $$              
                                                   \$$    $$              
                                                    \$$$$$$               

            
            """)
        
            else:
                raise ValueError(f"{player_response}")
        except ValueError as e:
            print(f"\nYou selected {e}. Please type 'Y' to play new round or 'N' to end game.")

def select_word():
    """
    Generates a random word from the words.py file. The player must guest
    this word. A new word is selected after each round.
    """
    random_word = random.choice(words).upper()
    return random_word

def graphics(image_of_lives):
    """
    The appropriate graphic below be presented to the user dependpent on
    how many lives the user has left. The user has six lives.
    """
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
              |     O
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
              |     O
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
              |     O
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
              |     O
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
              |     O
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