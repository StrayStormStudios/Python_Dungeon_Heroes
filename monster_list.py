from monster import Monster
import random

class MonsterList():
    def __init__(self):
        self.monsters = []       # the list of all possible monsters in the game
        self.addGiantRat()
        """
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
    
    # getmonster - -> returns a random monster form are list
    def get_monster(self):
        # return the monster
        return self.monsters[random.randint(0, len(self.monsters)-1)]

    #adds a Giant Rat monster
    def addGiantRat(self):
        name = "Giant Rat"
        desc = """A foul rat, as big as a small child rears up before you. it looks at you with hunger in it eyes.
            __       __
           /  \\_____/  \\
           | o       o |
            \\ (o) (o) /
             _| ___ |_
            / | ___ | \\
            | \\     / |
          ===== () =====
         / ||        || \\
        /   \\\\      //   \\
        |    ^^    ^^    |
        \\                /
         \\  _________   /==============-----
         ///         \\\\\\"""
        attack_desc = "bites You";

        level = 1;
        health = 5;
        attack = 8;
        damage = 2;
        defense = 10;
        protection = 1;
        speed = 12;

        xp = 10;
        gold = 5;
        food = 50;
        basic = 1;
        advanced = 0;
        epic = 0;

        temp = Monster(name, desc, attack_desc, level,
            health, attack, damage, defense, protection, speed,
            xp, gold, food, basic, advanced, epic);

        #adds to list    
        self.monsters.append(temp)