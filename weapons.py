class shortsword: # class for shortsword weapon
    damage = int(roll_dice(6))


class longsword:
    damage = int(roll_dice(8))



class weapons:

    shortsword = shortsword.damage
    longsword = longsword()


print(weapons.longsword)