from intro import intro 
from farewell import farewell
from rounds import print_round, get_quote, round_result, intermission

NUM_ROUNDS = 5

def main():
    """Runs main gaime loop with intro, rounds, and farewell."""

    # Intro
    intro_result = intro()
    if not intro_result["start_game"]:
        farewell(intro_result["player"])
        return
    
    player_character = intro_result["player"]

    # Rounds
    round_number = 1
    intermission_choice = "c"

    while round_number < NUM_ROUNDS and player_character.lives > 0 and intermission_choice != "q":
        print_round(round_number)
        quote_data = get_quote()
        philosopher = quote_data["philosopher"]
        quote = quote_data["quote"]
        philosophers = quote_data["philosophers"]

        while True:
            try:
                user_choice = int(input("\n> "))
                if 1 <= user_choice <= len(philosophers):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(philosophers)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        round_result(player_character, user_choice, quote, philosopher, philosophers)
        intermission_choice = intermission(player_character)
        round_number += 1
    
    # Farewell sequence
    farewell(player_character)
                    

    

if __name__ == "__main__":
    main()