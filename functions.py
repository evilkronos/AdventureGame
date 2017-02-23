import random
import characters
import time
import weapons


#  defines the dice rolling mechanic


def roll_dice(sides):
    return random.randint(1, sides)


welcome = print("Welcome to Dragons in a Dungeon. Text based game by Daniel Fischer")


def tutorial():
    print("A thug is standing before you about to attack! Rolling for initiative....")
    pc_init = 0
    npc_init = 0
    global att_order
    att_order = 0
    while pc_init == npc_init:  # initiative roll, while pc and npc are equal, reroll
        pc_init = roll_dice(20)
        npc_init = roll_dice(20)
    if pc_init > npc_init:
        time.sleep(1)
        print("You roll a " + str(pc_init) + ", your initiative roll was greater than your"
                                             "opponents, you attack first!")
        att_order = 1
    elif pc_init < npc_init:
        time.sleep(1)
        print("You roll a " + str(pc_init) + ", you attack second!")
        att_order1 = 2
    print(att_order)

    print("Lets fight!")
    print("Select action: attack, run")


def queueTutorial():
    print("If you would like to see the tutorial tpe: tutorial")
    if input() == 'tutorial': #template for a combat scenario
        tutorial()
    else: print("You have selected not to see how the combat looks")


def inputDice():
    input = [input()]
    print(input)


def inputRoll():

    acceptableDice = ['d6', 'd8', 'd10', 'd20', 'd100']
    print('Enter a dice to roll:')
    roll = input()

    if roll not in acceptableDice:
     print('You need to enter one of the above mentioned dice.')
    else:
        print("Rolling dice.....")
        time.sleep(2)
        str(roll_dice(int(roll)))
        time.sleep(.5)
        print("You rolled a " + str(roll_dice(int(roll))) + " congratulations on your first dice roll!")



