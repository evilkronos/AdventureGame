from functions import roll_dice

class Items():

    def __init__(self, name, price, attack, ac, weight):
        self.name = name
        self.price = price
        self.attack = attack
        self.ac = ac
        self.weight = weight


shortsword = Items('shortsword', 15, 6, 0, 10)

print(roll_dice(shortsword.attack))