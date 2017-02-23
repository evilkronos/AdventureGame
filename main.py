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
time.sleep(1)

functions.inputRoll()
time.sleep(1)

print("This game will run with a watered down version of the D&D dice roll system. You will "
      "roll for initiative each fight and then roll for attack against an armour class. "
      "On successful attack roll you will roll for damage which will be decided by your current weapon.")
functions.queueTutorial()
print("Lets continue!")

