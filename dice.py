import random

class Dice():
    #roll
    #returns an open ended 6 sided dice roll
    def roll(self=None):
        curRoll = random.randint(1, 6)  #number between 1 and 6
        total = curRoll
        #keep rolling, until we roll something that is not a six
        while(curRoll == 6):
            total = total - 1  # make total 5
            curRoll = random.randint(1, 6)  # new number between 1 and 6
            total = total + curRoll
        return total
