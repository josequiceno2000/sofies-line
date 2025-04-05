from collections import defaultdict
import textwrap

class Player:
    """
    Represents a player in sofie's line.
    Attributes:
        name (str): Player's chosen name.
        lives (int): Remaining lives.
        points (int): Accumulated points.
        enchiridion (defaultdict): Dictionary storing quotes seen by the player
    """

    INITIAL_LIVES = 3

    def __init__(self, name: str) -> None:
        """Initializes a new Player instance."""
        self.name: str = name
        self._lives: int = Player.INITIAL_LIVES
        self.points: int = 0
        self.enchiridion: defaultdict[str, list[str]] = defaultdict(list)
    
    @property
    def lives(self) -> int:
        """Gets player's remaining lives."""
        return self._lives

    def lose_life(self) -> None:
        """Makes player lose one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def gain_points(self, points: int) -> None:
        """Increases player points by prescribed amount."""
        self.points += points

    def gain_wisdom(self, phrase: str, author: str) -> None:
        """Updates enchiridion with new phrase."""
        self.enchiridion[author].append(phrase)
    
    def show_stats(self) -> None:
        """Displays the player's current stats with enhanced visual formatting."""
        width_display = 90
        print("\n" + "=" * width_display)
        print(f"⚡︎{self.name.upper()} STATS ⚡︎".center(width_display))
        print("=" * width_display)

        print(f"❤️ Lives: {self.lives}".center(width_display))
        print(f"✯ Points: {self.points}".center(width_display))

        print("\n📜 Enchiridion:")
        if self.enchiridion:
            for author, quotes in self.enchiridion.items():
                print("-" * width_display)
                print(f"  👤 {author}:")
                for quote in quotes:
                    wrapped_quote = textwrap.fill(quote, width=width_display - 10)
                    for line in wrapped_quote.splitlines():
                        if line == wrapped_quote.splitlines()[0]:
                            print(f"        » {line}")
                        else:
                            print(f"          {line}")
        else:
            print("   (Empty)")

        print("=" * width_display + "\n")