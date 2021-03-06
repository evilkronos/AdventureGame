import math

# Character class to define each character in the game.


class Characters:

    def __init__(self, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, basearmourclass, baseinitiative):
        self.name = name
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.baseArmourClass = basearmourclass
        self.baseInitiative = baseinitiative

#  Class to create the modifiers passed on Character's class

class Modifiers:

    def __init__(self, str, dex, con, int, wis, cha):
        self.str = math.floor((Player1.strength - 10) / 2)
        self.dex = math.floor((Player1.dexterity - 10) / 2)
        self.con = math.floor((Player1.constitution - 10) / 2)
        self.int = math.floor((Player1.intelligence - 10) / 2)
        self.wis = math.floor((Player1.wisdom - 10) / 2)
        self.cha = math.floor((Player1.charisma - 10) / 2)


Player1 = Characters('Rohnar VII', 3, 15, 11, 13, 9, 15, 10, 17, 1)
Player1mod = Modifiers(str=Player1.strength,dex=Player1.dexterity,con=Player1.constitution,int=Player1.intelligence,wis=Player1.wisdom,cha=Player1.charisma)


#  Below is the print example for chracter stat and modifier
#  print(Player1.strength, + Player1mod.str)
