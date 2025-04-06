from quotes import PHILOSOPHER_QUOTES
from player import Player
import random
import textwrap

ROUND_ART = {
        1: """
██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗      ██╗
██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗    ███║
██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║    ╚██║
██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║     ██║
██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝     ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝      ╚═╝""",
        2: """
██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗     ██████╗ 
██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗    ╚════██╗
██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║     █████╔╝
██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║    ██╔═══╝ 
██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝    ███████╗
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝     ╚══════╝""",
        3: """
██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗     ██████╗ 
██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗    ╚════██╗
██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║     █████╔╝
██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║     ╚═══██╗
██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝    ██████╔╝
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝     ╚═════╝""",
        4: """
██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗     ██╗  ██╗
██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗    ██║  ██║
██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║    ███████║
██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║    ╚════██║
██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝         ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝          ╚═╝""",
        5: """
██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗     ███████╗
██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗    ██╔════╝
██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║    ███████╗
██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║    ╚════██║
██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝    ███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝     ╚══════╝"""
    }

QUESTION_WIDTH = 80
RESULT_WIDTH = 37

def print_round(round_number: int) -> None:
    """Takes a round number and prints the appropriate ASCII art."""
    print(ROUND_ART.get(round_number, "Round Art Not Found")) 

def get_unique_random_philosophers(philosopher: str) -> list:
    """Returns a list of unique philosophers, including the given philosopher"""
    all_philosophers = list(PHILOSOPHER_QUOTES.keys())
    available_philosophers = [p for p in all_philosophers if p != philosopher]

    if len(available_philosophers) < 3:
        raise ValueError("Not enough philosophers to select 3 unique candidates.")
    
    random_philosophers = random.sample(available_philosophers, k=3)
    return random_philosophers + [philosopher]

def get_quote(difficulty: int, seen_quotes: list) -> dict:
    """
    Gets a random quote and sets up the question.

    Args:
        difficulty (int): Positive integer between 1 and 10 which dictates question difficulty.

    Returns:
        dict: Dict with philosopher, quote, and a list of possible philosophers.
    """

    eligible_quotes = []
    for philosopher, quotes in PHILOSOPHER_QUOTES.items():
        for quote_data in quotes:
            if quote_data["difficulty"] <= difficulty and quote_data["text"] not in seen_quotes:
                eligible_quotes.append({"philosopher": philosopher, "quote_data": quote_data})
    
    if not eligible_quotes:
        raise ValueError(f"No quotes found for difficult level {difficulty}.")

    chosen_quote = random.choice(eligible_quotes)
    philosopher = chosen_quote["philosopher"]
    quote = chosen_quote["quote_data"]["text"]
    philosophers = get_unique_random_philosophers(philosopher)

    print("=" * QUESTION_WIDTH + "\n")
    print("Who said:".center(QUESTION_WIDTH) + "\n")
    wrapped_quote = textwrap.fill(quote, width=QUESTION_WIDTH)
    print(wrapped_quote + "\n")
    print("=" * QUESTION_WIDTH + "\n")

    random.shuffle(philosophers)
    for index, author in enumerate(philosophers):
        print(f"[{index + 1}] {author}")

    return {"philosopher": philosopher, "quote": quote, "philosophers": philosophers}


def round_result(player_character: Player, user_choice: int, quote: str, philosopher: str, philosophers: list) -> None:
    """
    Displays the round results and updates player stats.

    Args:
        player_character (Player): The player character object.
        user_choice (int): The selected number representing a philosopher.
        quote (str): The philosophical quote in question. 
        philosopher (str): The rightful speaker of the quote.
        philosophers (list): List of potential speakers of the quote.
    """

    print("\n" + "=" * RESULT_WIDTH)
    if user_choice - 1 == philosophers.index(philosopher):
        result_statement = "Correct! [ +5 points ]"
        player_character.gain_points(5)
    else:
        result_statement = "Wrong! [ -1 Life ]"
        player_character.lose_life()
    print(result_statement.center(RESULT_WIDTH) + "\n")
    attribution = (f"The right answer was {philosopher.upper()}")
    print(attribution.center(RESULT_WIDTH) + "\n")
    enchiridion_update = ("*** Updating Enchiridion... ***")
    print(enchiridion_update.center(RESULT_WIDTH))
    print("=" * RESULT_WIDTH)

    player_character.gain_wisdom(quote, philosopher)

def intermission(player_character: Player) -> str:
    """Handles intermission choices."""

    while True:
        choice = input("\nSELECT: [s] Stats | [q] quit | [c] continue\n> ")
        if choice in ("s", "q", "c"):
            break
        else:
            print("Invalid choice. Please enter 's', 'q', or 'c'.")

    if choice == "s":
        player_character.show_stats()
        while True:
            choice2 = input("Ready to continue? [q] quit | [c] continue\n> ").lower()
            if choice2 in ("q", "c"):
                return choice2
            else:
                print("Invalid choice. Please enter 'q' or 'c'.")
        return choice2
    return choice