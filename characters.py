#from weapons import shortsword
#from items import Armour
#import functions
#import weapons
#import items


class Characters:

    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma, basearmourclass, baseinitiative):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.baseArmourClass = basearmourclass
        self.baseInitiative = baseinitiative


Player1 = Characters('kronos', 1, 2, 3, 4, 5, 6, 7, 10)


#Find way to call/make modifiers, eg: characters.self.intelligence -+ modifier



print(Player1.intelligence)


