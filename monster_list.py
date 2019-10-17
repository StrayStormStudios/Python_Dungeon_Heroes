#from dungeon_heroes import hero
import random

class MonsterList:
    monsters = []  # the list of all possible monsters in the game

    # getmonster - -> returns a random monster form are list
    def get_monster(self, hero):
        valid_monster = False
        result = 0
        while(not valid_monster):
            result = random.randint(len(monsters))
            if(monsters.get(result).level <= hero.level):
                valid_monster = True
        
        # return the monster
        return monsters.get(result)

    # constructor(constructs the  list of monsters)
    """def MonsterList():
        monsters = new ArrayList()
        addGiantRat()
        addCyclops()
        addAngry_Zombie()
        addFast_Zombie()
        addZombie()
        addDragon()
        addBaby_Dragon()
        addUnicorn()
        addTinyBat()
        addGiantSpider()
"""
