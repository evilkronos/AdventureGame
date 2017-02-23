from weapons import shortsword
from items import Armour
import functions


class ArmourClass:  #a rmourclass class for various NPC's default armourclass

    bandit = 13
    thug = 14
    soldier = 15
    knight = 17


class PC:  # statistics for the player controller

    pcArmourClass = 15
    pcMaxHealth = 15
    pcWeapon = shortsword.damage

# print(int(pc.pcWeapon))


class Bandit:

    ArmourClass.bandit
    maxHealth = 10
    weapon = shortsword.damage


class Thug:

    ArmourClass.thug
    maxHealth = 10
    weapon = shortsword.damage * 2
    armour = Armour.leather


class Soldier:

    ArmourClass.soldier
    maxHealth = 15
    weapon = weapons.longsword_attk
