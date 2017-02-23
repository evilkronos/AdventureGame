import random
#import characters
import time
#import weapons


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

    acceptableDice = ['6', '8', '10', '20', '100']
    print("Lets roll some dice to test the rolling. Enter a dice to roll from the following dice: 6, 8, 10, 20, 100")
    input_roll = input()

    while input_roll not in acceptableDice:
     print('You need to enter one of the above mentioned dice.')
     input_roll = input()
    else:
        print("Rolling dice.....")
        time.sleep(2)
        roll = (int(roll_dice(int(input_roll))))
        print(roll)
        time.sleep(.5)
        print("You rolled a " + str(roll) + ", congratulations on your first dice roll!")



