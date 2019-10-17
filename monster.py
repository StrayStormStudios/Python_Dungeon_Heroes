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
        self.desc = desc
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
        self.basic = basic
        self.advanced = advanced
        self.epic = epic
        
        #display
        self.__repr__()


#-------------------End init-------------------

    #singleAttack(Handles a single attack
    # @param Dice dice - -> a pointer to our dice
    # Player p - -> a pointer to the player
    # String response - -> the players response
    # @return - -> True if player ran successfully, False if not
    def singleAttack(self, dice, hero, response):
        # is the player trying to flee?
        if(response == "F"):
            # did the player run successfully? (Monster + Player will have roll off)
            if(hero.speed + dice.roll() > self.speed + dice.roll()):
                return True # the player ran away
            else :
                print("\nYou could not run Away...\n")
        else:
            # player is fighting
            attack = hero.attack # copy the attack
            strength = hero.strength # copy the players damage
            # is the player doing a strong attack?
            if(response.equals("S")):
                # does the player have enough stamina to make a strong attack?
                if(hero.stamina > 25):
                    hero.stamina -= 25
                    attack += 5
                    strength += 5
                else:
                    print("\nYou are too tired to make a Strong attack\n")
            # end strong attack block

            # generate the player's attack
            # check to see if the player misses
            if(attack + dice.roll() < self.defense + dice.roll()):
                print("You swing and miss!")
            else:
                damage = strength + dice.roll() - self.protection - dice.roll() # calculate damage
            if(damage <= 0): # deflected off armor
                print("You hit but cause no damage :(")
            else:
                # decrease monsters hit-points
                self.curHealth = self.curHealth - damage
                # celebrate the hit!
                print("You attack the {} and score a hit of {} damage. Monster's Health: ({}/{})".format(self.name, damage, self.curHealth, self.health))
                # end damage calculation
            # ends the hit / miss block
        # closes running block

        # Monsters Attack
        monster_attack= self.attack + dice.roll() - hero.defense - dice.roll()
        monster_damage= self.damage + dice.roll() - hero.protection - dice.roll()
        # did the monster miss?
        if(monster_attack < 0):
            print("The {} {} but misses.".format(self.name, self.attack_desc))
        else:
            # did they do damage
            if(monster_damage < 0):
                print("The {} {} but does no damage.".format(self.name, self.attack_desc))
            else:                # they did damage
                hero.health -= monster_damage
                print("The {} {} and does {} damage! Your health is now: ({}/{})".format(
                    self.name, self.attack_desc, monster_damage, hero.health, hero.maxHealth))
            # end the damage block
        # end the hit block
        return False


#-------------------End attack-------------------

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

    """def __repr__(self):
        print(""{} has
        {}/{} hp, stamina {}/{}, & their:
        description is:\t {}
        defense is:\t {}
        armor is:\t {}
        and speed of:\t {}
        "".format(self.name, self.health, self.current_health, self.stamina, self.max_stamina, self.description, self.defense, self.protection, self.speed))
"""