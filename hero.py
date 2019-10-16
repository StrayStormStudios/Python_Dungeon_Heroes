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
        maxStamina:         int
        food:               int     used to rest and regain health .format( stamina
        maxFood:            int
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
        self.health = 100
        self.maxHealth = self.health
        self.stamina = 50
        self.maxStamina = self.stamina
        self.maxFood = 63
        self.food = self.maxFood
        self.gold = 0
        
        #attack attributes
        self.attack = 2
        self.strength = 0
        
        #defense attributes
        self.defense = 2
        self.protection = 0
        
        #speed
        self.speed = 1

        #display
        self.__repr__()

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
      print("Health: {}/{}".format(self.health, self.maxHealth))
      print("Stamina: {}/{}".format(self.stamina, self.maxStamina))
      print("Food: {}/{}".format(self.food, self.maxFood))
      print()
      print("Attack: {}".format(self.attack))
      print("Strength: {}".format(self.strength))
      print("Defense:{}".format(self.defense))
      print("Armor: {}".format(self.protection))
      print("Speed: {}".format(self.speed))
      print()
    
    #give_food - -> gives food to the player
    def give_food(self, food):
        self.food += food
        print("Food Looted: {}! Your new total is: {}".format(food, self.food))
        return self.food
    
    #give_gold --> gives gold to the player
    def give_gold(self, gold):
        self.gold += gold
        print("Gold Looted: {}! Your new total is: {}".format(gold, self.gold))
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
            self.maxHealth+= 2 #add 2 to max health
            self.health = self.maxHealth # set health to max health
            #self.levelUp = self.levelUp #activates level up perks

    def __repr__(self):
        print("""{} has
        {}/{} hp, stamina {}/{}, & their:
        strength is:\t {}
        defense is:\t {}
        armor is:\t {}
        and speed of:\t {}
        """.format(self.name, self.health, self.maxHealth, self.stamina, self.maxStamina, self.strength, self.defense, self.protection, self.speed))
