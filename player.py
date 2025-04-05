class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.points = 0
        self.enchiridion = {}
    
    def lose_life(self):
        self.lives -= 1
    
    def gain_points(self, points):
        self.points += points

    def gain_wisdom(self, phrase, author):
        if author in self.enchiridion:
            if phrase not in self.enchiridion[author]:
                self.enchiridion[author].append(phrase)
        else:
            self.enchiridion[author] = [phrase]
    
    def show_stats(self):
        print()
        print(f"\n[{self.name.upper()} STATS]")
        print(f"• Lives: {self.lives}")
        print(f"• Total Points: {self.points}")
        print("• Enchiridion: ")
        for author in self.enchiridion.keys():
            print(f"\t» {author}:")
            for quote in self.enchiridion[author]:
                print(f"\t\t»» {quote}")