from quotes import philosopher_quotes
import random
import textwrap

def get_quote():
    philosophers = list(philosopher_quotes.keys())
    philosopher = random.choice(philosophers)
    quote = random.choice(philosopher_quotes[philosopher])

    width = 80

    print()
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
    print("\n" + "=" * 31)
    if user_choice - 1 == philosophers.index(philosopher):
        correct_statement = "[ Correct! +5 points ]"
        print(correct_statement.center(31))
        player_character.gain_points(5)
    else:
        wrong_statement = "[ Wrong! -1 Life ]"
        print(wrong_statement.center(31))
        player_character.lose_life()
    print("*** Updating Enchiridion... ***")
    print("=" * 31)
    player_character.gain_wisdom(quote, philosopher)

    print()
    print(f"\n[{player_character.name.upper()} STATS]")
    print(f"- Lives: {player_character.lives}")
    print(f"- Total Points: {player_character.points}")
    print(f"- Enchiridion: {player_character.enchiridion}")