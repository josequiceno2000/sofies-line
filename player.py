class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.wrong = 0
        self.points = 0
        self.enchiridion = []
    
    def add_correct(self):
        self.correct += 1
    
    def add_wrong(self):
        self.wrong += 1
    
    def gain_points(self, points):
        self.points += points

    def gain_wisdom(self, phrase, author):
        self.enchiridion.append([phrase, author])