import time
import functions
from functions import *
#import items
#import characters
#import weapons
#from functions import roll_dice


#print(functions.welcome)
print('Are you ready for an adventure? Please enter your name:')
pcName = input()

print('Good job entering your name ' + (str(pcName)))
print('Let me test some dice rolls!')
print('What dice would you like to roll? Type either: 6, 8, 10, 20 or a 100')

diceInput = input()
print("Rolling dice.....")
time.sleep(2)

functions.inputRoll()
#  print("You rolled a " + str(roll_dice(int(diceInput))) + " congratulations on your first dice roll!")
time.sleep(1)

print("This game will run with a watered down version of the D&D dice roll system. You will "
      "roll for initiative each fight and then roll for attack against an armour class. "
      "On successful attack roll you will roll for damage which will be decided by your current weapon.")
functions.queueTutorial()
print("Lets continue!")

