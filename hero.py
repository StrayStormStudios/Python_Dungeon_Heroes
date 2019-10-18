from monster_list import MonsterList
from prompts import prompt_usr

class Hero():
    def __init__(self, name, character_class=None):
        """Attributes (fields)
        --Main Attributes
        name:               String
        character_class:    String
        level:              init
        levelUp:            boolean
        xp:                 init
        
        --life attributes
        health:             int     #If self goes to 0, game over
        maxHealth:          int
        stamina:            int     #used for special attacks
        max_stamina:         int
        food:               int     used to rest and regain health & stamina
        max_food:            int
        gold:               int     #amount of gold the player has
        
        --attack attributes
        attack:             int     #used to hit things
        strength:           int     #added to weapon damage to do damage
        
        --defense attributes
        defense:            int    #used to dodge
        protection:         int    #used to soak damage
        
        --speed
        speed:              int    #used to run away
        hands:              int    #the number of hands the player has left to equip items
        """
        #basic stats
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.xp = 0
        
        #life stats
        self.max_food = 100
        self.max_stamina = 100
        self.max_health = 10
        self.food = self.max_food
        self.health = self.max_health
        self.stamina = self.max_stamina
        self.gold = 0
        
        #attack attributes
        self.attack = 10
        self.strength = 1
        
        #defense attributes
        self.defense = 10
        self.protection = 1
        
        #speed
        self.speed = 10

        #display
        #self.__repr__()

#-------------------End init-------------------

    def set_health(self, new_health):
        self.health = new_health

    #stats - -> prints the status of the player
    def stats(self):
      print()
      print("Name: {}".format(self.name))
      print("Class: {}".format(self.character_class))
      print("Level: {}".format(self.level))
      print("Experience: {}".format(self.xp))
      print("Experience needed: {}".format((self.level * 10)))
      print()
      print("Health: {}/{}".format(self.health, self.max_health))
      print("Stamina: {}/{}".format(self.stamina, self.max_stamina))
      print("Food: {}/{}".format(self.food, self.max_food))
      print()
      print("Attack: {}".format(self.attack))
      print("Strength: {}".format(self.strength))
      print("Defense:{}".format(self.defense))
      print("Armor: {}".format(self.protection))
      print("Speed: {}".format(self.speed))
      print()
    
    #give_food - -> gives food to the player
    def give_food(self, food):
        if self.food < self.max_food:
            self.food += food
            print("Food Looted: {}! Your new total is: {}".format(food, self.food))
        else:
            print("You have the max amount of food you can hold")
        self.print_food()
        return self.food
    
    #give_gold --> gives gold to the player
    def give_gold(self, gold):
        self.gold += gold
        print("Gold Looted: {}! Your new total is: {}".format(gold, self.gold))
        self.print_money()
        return self.gold
   
    #give_XP --> gives xp to the player
    def give_XP(self, xp):
        self.xp += xp
        print("XP Gained: {}! Your new total is: {} of {}".format(xp, self.xp, (self.level*10)))
        self.level_up()
        return self.xp

    #level_up -->levels up the player
    def level_up(self):
        #do they have enough xp to level?
        if(self.xp >= self.level*10):       #level them up
            self.level+= 1 #add one to level
            print("You become Level {}!".format(self.level))
            self.xp = 0  #set xp to zero
            self.attack+= 1 #add one to attack
            self.defense+= 1 #add one to defense
            self.speed-= 1 #the player gets slower
            self.max_health+= 2 #add 2 to max health
            self.health = self.max_health # set health to max health
            #self.levelUp = self.levelUp #activates level up perks

#-------------------End Display, Collectables, and Level up-------------------
    #fight_monster - rolls a random monster and simulates fight
    #@param - -> input - a scanner console input
    #@return - -> int (epic treasures in 100s column, Advanced treasures in 10s column, basic treasures in the 1s column, -1 player dead)
    def fight_monster(self):
        monster_list = MonsterList()
        valid_monster = False
        while(not valid_monster):
            cur_monster = monster_list.get_monster()
            if(cur_monster.level <= self.level):
                valid_monster = True
        cur_monster.cur_health = cur_monster.health
        # copy the monsters health
        print("You come face to face with a {}".format(cur_monster.name))
        print(cur_monster.desc)
        print("The {} is poised, ready to attack!".format(cur_monster.name))
        if(self.level >= cur_monster.level):
            print("\n***********************")
            print("Good Monster: {}".format(cur_monster.name))
        else:
            print("\n***********************")
            print("Bad Monster: {}".format(cur_monster.name))

        print("player level: {}".format(self.level))
        print("Monster level: {}".format(cur_monster.level))
        print("***********************\n")
        # calculate potential treasure
        treasure = cur_monster.epic * 100 + cur_monster.advanced * 10 + cur_monster.basic

        # main fighting loop
        keep_fighting = True
        # should we keep fighting
        while(keep_fighting):
            # get their input
            valid_input = False
            response = ""
            while(not valid_input):
                print("\nMonster's HP: {}/{} \t Your HP: {}/{}".format(cur_monster.cur_health, cur_monster.health, self.health, self.max_health))
                response = prompt_usr("Do you want to (F)lee, make a (S)strong attack, or make a (W)eak attack? \t", "string").upper()
                if(response == "F" or response == "S" or response == "W"):
                    # it is a valid response
                    valid_input = True
                else:
                    print("Invalid input!")
            # end validInput while

            # generate an attack
            flee = cur_monster.singleAttack(self, response)
            # handles one attack
            # did the player flee?
            if(flee):
                print("\nYou manage to flee!\n")
                # no treasure
                return 0
            # did the player die?
            elif(self.health <= 0):
                # the player died
                print("\nYou have been slain by a {}".format(cur_monster.name))
                print("Total Gold: {}, Total Level {}".format(self.gold, self.level))
                print("Better luck next time!\n")
                return -1
            # did the player win?
            elif(cur_monster.cur_health <= 0):
                print("\n*************************************")
                print("You vanquish the {}".format(cur_monster.name))
                print("Your Health: {}".format(self.health))

                # reward with food, gold and xp
                self.give_food(cur_monster.give_food())
                self.give_gold(cur_monster.give_gold())
                self.give_XP(cur_monster.xp)
                return cur_monster.get_treasure()
        #end keepFight while
        return -1

    #rest - -> handles resting(if enough food)
    def rest(self):
        #heal health first
        #do they have enough food?
        if(self.food >= (self.max_health - self.health) * 10):
            self.food = self.food - (self.max_health - self.health) * 10  #enough food to completely heal
            self.health = self.max_health
            print("\nYou completely heal up! HEALTH: {}".format(self.health))
        elif(self.food > 0):
            self.health = self.health + self.food / 10
            self.food = 0
            print("\nYou only have enough food to partially restore your health. HEALTH: {}".format(self.health))
        else :
            print("\nYou are out of food and cannot regain health. HEALTH: {}".format(self.health))
        
        #heal stamina
        #do they have enough food?
        if(self.food >= (self.max_stamina - self.stamina)):
            # enough food to completely fill stamina
            self.food = self.food - (self.max_stamina - self.stamina)
            self.stamina = self.max_stamina
            print("\nYou completely regain your stamina. STAMINA: {}".format(
                self.stamina))
        elif(self.food > 0):
            self.stamina = self.stamina + self.food
            self.food = 0  # partially fill stamina
            print("\nYou only have enough food to partially regain your stamina. STAMINA: {}".format(
                self.stamina))
        else:
            print("\nYou are out of food and cannot regain stamina. STAMINA: {}".format(
                self.stamina))

        self.print_food()
        print("Food remaining: {}".format(self.food))

    def __repr__(self):
        print("""{} has
        {}/{} hp, stamina {}/{}, & their:
        strength is:\t {}
        defense is:\t {}
        armor is:\t {}
        and speed of:\t {}
        """.format(self.name, self.health, self.max_health, self.stamina, self.max_stamina, self.strength, self.defense, self.protection, self.speed))

    def print_food(self):
        print("""
                                .-'''''-.
                                |'-----'|
                                |-.....-|
                                |       |
                                |       |
            _,._                |       |
        __.o`   o`\"-.           |       |
    .-O o `\"-.o   O )_,._    |       |   
    ( o   O  o )--.-\"`O   o\"-.`'-----'`
    '--------'  (   o  O    o)
                    `----------`    """)

    def print_money(self):
        print("""
              \\`\\/\\/\\/`/
               )======(
             .'        '.
            /    _||__   \\
           /    (_||_     \\
          |     __||_)     |
          |       ||       |
          '.              .'
            '------------'      """)
