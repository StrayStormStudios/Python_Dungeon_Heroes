from dice import Dice as dice
import random

class Monster():
    def __init__(self, name=None, desc="I'm a monster", attack_desc=None, level=0, health=10, attack=0, damage=0,
    defense=0, protection=0, speed=0, xp=10, gold=10, food=10, basic=0, advanced=0, epic=0):
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
        
        --treasure fields
        xp:                     int
        gold:                   int         amount of gold the player has
        food:                   int         used to rest and regain health
        """
        #main stats
        self.name = name
        self.desc = desc
        self.attack_desc = attack_desc
        self.level = level
        self.health = health
        self.current_health = self.health
        
        #attack attributes
        self.attack = attack
        self.damage = damage
        
        #defense attributes
        self.defense = defense
        self.protection = protection
        
        #speed
        self.speed = speed

        #treasure fields
        self.xp = xp
        self.food = food
        self.gold = gold
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
    def singleAttack(self, hero, response):
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
            if(response == "S"):
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
                print("You are Capable of {} Damage".format(damage))
                if(damage <= 0): # deflected off armor
                    print("You hit but cause no damage :(")
                else:
                    # decrease monsters hit-points
                    self.cur_health -= damage
                    # celebrate the hit!
                    print("You attack the {} and score a hit of {} damage. Monster's Health: ({}/{})".format(self.name, damage, self.cur_health, self.health))
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
                    self.name, self.attack_desc, monster_damage, hero.health, hero.max_health))
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
        basic = random.randint(-1, self.basic)
        advanced = random.randint(-1, self.advanced)*10
        epic = random.randint(-1, self.epic)*100

        treasure = basic + advanced + epic
        return treasure

    """def __repr__(self):
        print(""{} has
        {}/{} hp, & their:
        description is:\t {}
        defense is:\t {}
        armor is:\t {}
        and speed of:\t {}
        "".format(self.name, self.health, self.current_health, self.description, self.defense, self.protection, self.speed))
"""