import Character

class Monster:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def Attack(self):
        Character.Character.health = Character.Character.health - self.attack


