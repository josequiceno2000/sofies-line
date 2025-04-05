from intro import intro 
from farewell import farewell
from rounds import print_round, get_quote, round_result, intermission

def main():
    # Intro
    player_character, start_game = intro()

    if start_game:
        # Rounds
        round_number = 1
        intermission_choice = "c"

        while round_number < 6 and player_character.lives > 0 and intermission_choice != "q":
            print_round(round_number)
            philosopher, quote, philosophers = get_quote()
            user_choice = int(input("\n> "))
            round_result(player_character, user_choice, quote, philosopher, philosophers)
            intermission_choice = intermission(player_character)
            round_number += 1
    
    # Farewell sequence
    farewell(player_character)
                    

    

if __name__ == "__main__":
    main()