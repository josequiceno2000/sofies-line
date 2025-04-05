from quotes import philosopher_quotes
import random
import textwrap

def get_quote():
    philosopher = random.choice(list(philosopher_quotes.keys()))
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
    print("\n[a] Aristotle\n[b] Aquinas\n[c] Albertus Magnus\n[d] Socrates\n[e] Plato\n")
    