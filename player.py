class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.points = 0
        self.enchiridion = []
    
    def lose_life(self):
        self.lives -= 1
    
    def gain_points(self, points):
        self.points += points

    def gain_wisdom(self, phrase, author):
        self.enchiridion.append([phrase, author])