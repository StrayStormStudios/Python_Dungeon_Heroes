from monster import Monster
import random

class MonsterList():
    def __init__(self):
        self.monsters = []       # the list of all possible monsters in the game
        self.addGiantRat()
        self.addCyclops()
        self.addAngry_Zombie()
        self.addFast_Zombie()
        self.addZombie()
        self.addDragon()
        self.addBaby_Dragon()
        self.addUnicorn()
        self.addTinyBat()
        self.addGiantSpider()
    
    # getmonster - -> returns a random monster form are list
    def get_monster(self):
        # return the monster
        return self.monsters[random.randint(0, len(self.monsters)-1)]

    #adds a Giant Rat monster
    def addGiantRat(self):
        name = "Giant Rat"
        desc = """A foul rat, as big as a small child rears up before you. it looks at you with hunger in it eyes.
            __       __
           /  \_____/  \\
           | o       o |
            \ (o) (o) /
             _| ___ |_
            / | ___ | \\
            | \     / |
          ===== () =====
         / ||        || \\
        /   \        /   \\
        |    ^^    ^^    |
        \                /
         \  _________   /==============-----
         ///         \\\\\\ """
        attack_desc = "bites at You"

        level = 1
        health = 5
        attack = 8
        damage = 2
        defense = 10
        protection = 1
        speed = 12

        xp = 10
        gold = 5
        food = 50
        basic = 1
        advanced = 0
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
            health, attack, damage, defense, protection, speed,
            xp, gold, food, basic, advanced, epic)

        #adds to list    
        self.monsters.append(temp)

    #adds a MicroScopic Bat monster
    def addTinyBat(self):
        name = "Tiny Bat"
        desc = """A microscopic bat, as small as a grain of salt rears down before you. it looks at you with hunger in it eyes.
            /(    )\\
            |  -^^-  |
            \\_ `' _/
                \\  )
                )/
                ('     """
        attack_desc = "bites You"

        level = 1
        health = 5
        attack = 5
        damage = 1
        defense = 8
        protection = 1
        speed = 16

        xp = 10
        gold = 5
        food = 50
        basic = 1
        advanced = 0
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #adds to list
        self.monsters.append(temp)

    #adds a Ga Spider monster
    def addGiantSpider(self):
        name = "Giant Spider"
        desc = "A hideous Spider, as big as a small child rears up before you. it looks at you with hunger in it eyes."
        attack_desc = "bites You"

        level = 1
        health = 10
        attack = 10
        damage = 5
        defense = 8
        protection = 4
        speed = 8

        xp = 30
        gold = 15
        food = 100
        basic = 2
        advanced = 0
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #adds to list
        self.monsters.append(temp)

    #adds a Cyclops monster
    def addCyclops(self):
        name = "Cyclops"
        desc = "A twenty foot tall ga peers menacingly at you with his single large eye."
        attack_desc = "swings his hammer at you"

        level = 10
        health = 50
        attack = 18
        damage = 20
        defense = 8
        protection = 15
        speed = -5

        xp = 300
        gold = 2000
        food = 1000
        basic = 0
        advanced = 1
        epic = 1

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds an Angry_Zombie monster
    def addAngry_Zombie(self):
        name = "Angry Zombie"
        desc = "A Once Living person got lost in this dungeon with firends that angered him and he has been wondering around looking for BRAINS!!"
        attack_desc = "Swings Branch at you"

        level = 4
        health = 35
        attack = 20
        damage = 12
        defense = 10
        protection = 2
        speed = 5

        xp = 150
        gold = 150
        food = 10
        basic = 2
        advanced = 2
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds a Zombie monster
    def addZombie(self):
        name = "Zombie"
        desc = "A Once Living person got lost in this dungeon and has been wondering around looking for BRAINS!!"
        attack_desc = "swings his arms at you"

        level = 2
        health = 20
        attack = 10
        damage = 5
        defense = 5
        protection = 2
        speed = 5

        xp = 150
        gold = 100
        food = 10
        basic = 3
        advanced = 1
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds a Fast_Zombie monster
    def addFast_Zombie(self):
        name = "Fast Zombie"
        desc = "A Once Living athlete got lost in this dungeon and has been wondering around looking for BRAINS!!"
        attack_desc = "swings his arms at you"

        level = 3
        health = 20
        attack = 5
        damage = 5
        defense = 5
        protection = 5
        speed = 20

        xp = 50
        gold = 100
        food = 10
        basic = 3
        advanced = 1
        epic = 0

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds a Dragon monster
    def addDragon(self):
        name = "Dragon"
        desc = "This mystical creature is asleep... it awakens will you be burnt to a crisp!!"
        attack_desc = "Blows Fire at you"

        level = 15
        health = 400
        attack = 200
        damage = 170
        defense = 150
        protection = 60
        speed = 0

        xp = 3000
        gold = 1000
        food = 160
        basic = 1
        advanced = 2
        epic = 5

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds a Baby_Dragon monster
    def addBaby_Dragon(self):
        name = "Baby Dragon"
        desc = "This mystical creature is asleep... it awakens will you be burnt to a crisp."
        attack_desc = "Blows Fire at you"

        level = 10
        health = 200
        attack = 100
        damage = 85
        defense = 75
        protection = 30
        speed = 1

        xp = 1500
        gold = 500
        food = 80
        basic = 0
        advanced = 3
        epic = 2

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)

    #adds a Unicorn monster
    def addUnicorn(self):
        name = "Unicorn"
        desc = "This mystical creature has been locked down here for ages and so it is easily angered buy the slightest movement."
        attack_desc = "Stabs You With It's Horn"

        level = 15
        health = 200
        attack = 100
        damage = 85
        defense = 75
        protection = 15
        speed = 8

        xp = 500
        gold = 250
        food = 65
        basic = 3
        advanced = 1
        epic = 1

        temp = Monster(name, desc, attack_desc, level,
                        health, attack, damage, defense, protection, speed,
                        xp, gold, food, basic, advanced, epic)

        #add list
        self.monsters.append(temp)
