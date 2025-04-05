from intro import intro 
from rounds import get_quote, round_result

def main():
    # Intro
    player_character = intro()

    # Rounds
    philosopher, quote, philosophers = get_quote()
    user_choice = int(input("\n> "))
    round_result(player_character, user_choice, quote, philosopher, philosophers)
                

    

if __name__ == "__main__":
    main()