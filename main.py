from intro import intro 
from rounds import get_quote, round_result

def main():
    # Intro
    player_character = intro()

    # Rounds
    philosopher, quote, philosophers = get_quote()
    user_choice = int(input("\n> "))
    if round_result(user_choice, philosopher, philosophers):
        player_character.gain_points(5)
    else:
        player_character.lose_life()
    player_character.gain_wisdom(quote, philosopher)

    print()
    print(f"\n[{player_character.name.upper()} STATS]")
    print(f"- Lives: {player_character.lives}")
    print(f"- Total Points: {player_character.points}")
    print(f"- Enchiridion: {player_character.enchiridion}")

if __name__ == "__main__":
    main()