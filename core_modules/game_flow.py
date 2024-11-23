# Orchestrates the overall sequence of the game from start to finish.
# Manage the main game loop.
# Check win/loss conditions and terminate the game when appropriate.
# Restart or quit the game upon completion.

from core_modules.game_logic import play_game
from core_modules.word_selection import load_word_list
from core_modules.display_output import display_message


def start_game():
    """Handles the overall flow of the game."""
    display_message("Starting the game...")

    try:
        # Load word list from the external file
        word_list = load_word_list("assets/word_list.txt")
        if not word_list:
            display_message("Error: The word list is empty.")
            return

        # Start the Hangman game
        play_game(word_list)

    except FileNotFoundError:
        display_message(
            "Error: Word list file not found. Ensure 'assets/word_list.txt' exists."
        )
    except Exception as e:
        display_message(f"An unexpected error occurred: {e}")
