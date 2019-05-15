import random, main, Monster

r1 = random.Random()

class Room:
    def __init__(self, roomLevel):
        self.amountOfMonsters = r1.randint(roomLevel, roomLevel+2)
        self.monsters = []

    def addMonster(self):
        i = 0
        while i < self.amountOfMonsters:
            self.monsters[i] = Monster.Monster(100,5)
            i+=1

    def displayMonsters(self):
        for monster in self.monsters:
            print(monster + "/n")
