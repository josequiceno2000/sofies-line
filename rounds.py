from quotes import philosopher_quotes
import random
import textwrap

def print_round(round_number):
    round_map = {
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

    print(round_map[round_number]) 


def get_quote():
    philosophers = list(philosopher_quotes.keys())
    philosopher = random.choice(philosophers)
    quote = random.choice(philosopher_quotes[philosopher])

    width = 80

    print("=" * width)
    print()
    centered_question = "Who said:".center(width)
    centered_quote = f"{quote}".center(width)
    wrapped_quote = textwrap.fill(centered_quote, width=width)
    print(centered_question)
    print()
    print(wrapped_quote)
    print()
    print("=" * width)

    random.shuffle(philosophers)
    print()
    for i in range(len(philosophers)):
        print(f"[{i + 1}] {philosophers[i]}")

    return (philosopher, quote, philosophers)
    
def round_result(player_character, user_choice, quote, philosopher, philosophers):
    print("\n" + "=" * 37)
    if user_choice - 1 == philosophers.index(philosopher):
        result_statement = "Correct! [ +5 points ]"
        player_character.gain_points(5)
    else:
        result_statement = "Wrong! [ -1 Life ]"
        player_character.lose_life()
    print(result_statement.center(37))
    print()
    attribution = (f"The right answer was {philosopher.upper()}")
    print(attribution.center(37))
    print()
    enchiridion_update = ("*** Updating Enchiridion... ***")
    print(enchiridion_update.center(37))
    print("=" * 37)
    player_character.gain_wisdom(quote, philosopher)

def intermission(player_character):
    intermission_choice = input("\nSELECT: [s] Stats | [q] quit | [c] continue\n> ")

    if intermission_choice == "s":
        player_character.show_stats()
        print("\nReady to continue?")
        intermission_choice = input("SELECT: [q] quit | [c] continue\n> ")
        
    return intermission_choice
    