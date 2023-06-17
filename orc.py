import random
class Orc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 0
        self.direction = random.choice(["right", "left", "up", "down"])
        self.alive = True
        self.lives = 55
        self.image = None
