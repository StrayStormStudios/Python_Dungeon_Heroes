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
        health:             int     #If this goes to 0, game over
        maxHealth:          int
        stamina:            int     #used for special attacks
        maxStamina:         int
        food:               int     used to rest and regain health + stamina
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
        self.name = name;
        self.character_class = character_class;
        self.level = 1;
        self.xp = 0;
        
        #life stats
        self.health = 100;
        self.maxHealth = self.health;
        self.stamina = 50
        self.maxStamina = self.stamina;
        self.maxFood = 63
        self.food = self.maxFood;
        self.gold = 0;
        
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

    def __repr__(self):
        print("""{} has
        {}/{} hp, stamina {}/{}, & there:
        strength is:\t {}
        defense is:\t {}
        and speed of:\t {}
        """.format(self.name, self.health, self.maxHealth, self.stamina, self.maxStamina, self.strength, self.defense, self.speed))