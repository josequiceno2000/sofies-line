from intro import intro 
from rounds import print_round, get_quote, round_result

def main():
    # Intro
    player_character = intro()

    # Rounds
    round_number = 1

    while round_number < 6 and player_character.lives > 0:
        print_round(round_number)
        philosopher, quote, philosophers = get_quote()
        user_choice = int(input("\n> "))
        round_result(player_character, user_choice, quote, philosopher, philosophers)
        round_number += 1
                

    

if __name__ == "__main__":
    main()