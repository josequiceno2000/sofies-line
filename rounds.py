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
    
def round_result(user_choice, philosopher, philosophers):
    if user_choice - 1 == philosophers.index(philosopher):
        return True   
    return False