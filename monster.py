import random

class Monster():
    def __init__(self, name=None, desc="I'm a monster", attack_desc=None, level=1, health=100, attack=10, damage=10,
    defense=10, protection=0, speed=2, xp=10, gold=10, food=10, basic=0, advanced=0, epic=0):
        """Attributes (fields)
        --Main Attributes
        name:                   String
        description:            String
        attack description:     String
        level:                  int
        health:                 int
        current_health:         int         If this goes to 0, game over
        --attack attributes
        attack:                 int         used to hit things
        damage:                 int         added to weapon damage to do damage
        --defense attributes
        defense:                int         used to dodge
        protection:             int         used to soak damage
        --speed
        speed:                  int         used to run away
        
        --life attributes
        stamina:                int         used for special attacks
        maxStamina:             int
        maxFood:                int

        --treasure fields
        xp:                     int
        gold:                   int         amount of gold the player has
        food:                   int         used to rest and regain health
        """
        #main stats
        self.name = name
        self.description = desc
        self.attack_description = attack_desc
        self.level = 1
        self.health = 100
        self.current_health = self.health
        
        #attack attributes
        self.attack = 2
        self.damage = 0
        
        #defense attributes
        self.defense = 2
        self.protection = 0
        
        #speed
        self.speed = 1

        #life stats
        self.max_food = 40
        self.max_stamina = 10
        self.stamina = self.max_stamina

        #treasure fields
        self.xp = 0
        self.food = self.max_food
        self.gold = 0
        self.basic = basic;
        self.advanced = advanced;
        self.epic = epic;
        
        #display
        self.__repr__()

#-------------------End init-------------------

    #stats - -> prints the status of the player
    def stats(self):
      print()
      print("Name: {}".format(self.name))
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

    def set_health(self, new_health):
        self.current_health = new_health

    #give gold - -> returns the amount of gold the monster drops
    def give_gold(self):
        return random.randint(0, self.gold)

    #give food - -> returns the amount of food the monster drops
    def give_food(self):
        return random.randint(0, self.food)

    #returns the treasure randomly
    def get_treasure(self):
        basic = random.randint(self.basic)
        advanced = random.randint(self.advanced)*10
        epic = random.randint(self.epic)*100

        treasure = basic + advanced + epic
        return treasure

    def __repr__(self):
        print("""{} has
        {}/{} hp, stamina {}/{}, & their:
        description is:\t {}
        defense is:\t {}
        armor is:\t {}
        and speed of:\t {}
        """.format(self.name, self.health, self.current_health, self.stamina, self.max_stamina, self.description, self.defense, self.protection, self.speed))
