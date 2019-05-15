from monster import Monster

class Character:
    def __init__(self, health, attack, points):
        self.health = health
        self.attack = attack
        self.points = points

    def Attack(self, Monster):
        Monster.health = Monster.health - self.attack
        