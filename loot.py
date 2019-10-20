from item import Item
import random

#Loot class - stores lists of loot and returns random loot to the player
class Loot():
    # constructor
    def __init__(self):
        # set up lists
        self.epicItems = []
        # stores epic items
        self.advancedItems = []
        # stored advanced items
        self.basicItems = []
        # store basic items
        #private Random rand
        # random number generator

        # LEVEL 1 - 5
        # Weapons
        # basic
        self.addBranch()
        self.addDagger()
        # advanced
        self.addLongSword()
        # self.addIronSword()
        # epic
        self.addClaymore()
        self.addFlamingSword()
        # Armor
        # basic
        self.addLeatherArmor()
        # advanced
        self.addIronArmor()
        # epic
        # self.addSteal()
        # Misc
        # basic

        # advanced

        # epic

        """  # Level 5 - 10
        # Weapons
        # basic
            self.addSabre()
            self.addFalchion()
        # advanced
            self.addSmallMace()
            self.addLargeMace()
        # epic
            self.addWarHammer()
        # Armor
        # basic
            self.addGoldFlex()
        # advanced
            self.addChainMail()
        # epic
            self.addKevlar()
            # Misc
        # basic

        # advanced

        # epic

        # Level 10 - 15
        # Weapons
        # basic
            self.addDualDagger()
        # advanced
            self.addShortSword()
            self.addDualShortSword()
        # epic
            self.addDualLongSword()
        # Armor
        # basic
            self.addDendraPanoply()
        # advanced
            self.addDragonSkin()
        # epic
            self.addScaleArmor()
        # Misc
        # basic

        # advanced

        # epic
            """

    def getItem(self, uniqueID):
        for i in self.basicItems:
            if(i.uniqueID == uniqueID):
                return i

        for i in self.advancedItems:
            if(i.uniqueID == uniqueID):
                return i

        for i in self.epicItems:
            if(i.uniqueID == uniqueID):
                return i

        return getItem(uniqueID)

    def getEpic(self, hero):
        valid_loot = False
        i = 0

        while(not valid_loot):
            i = random.randint(len(self.epicItems))
            if(self.epicItems[i].findLevel <= hero.level):
                valid_loot = True

        return self.epicItems.get(i)

    def getAdvanced(self, hero):
        valid_loot = False
        i = 0

        while(not valid_loot):
            i = random.randint(len(self.advancedItems))
            if(self.advancedItems[i].findLevel <= hero.level):
                valid_loot = True

        return self.advancedItems.get(i)

    def getBasic(self, hero):
        valid_loot = False
        i = 0

        while(not valid_loot):
            i = random.randint(len(self.basicItems))
            if(self.basicItems[i].findLevel <= hero.level):
                valid_loot = True

        return self.basicItems.get(i)

    # LEVEL 1 - 5
    # ****Weapons****
    # ---basic---
    def addBranch(self):
        name = "Branch          "
        # ends in 8... helps inventory
        desc = "An old decaying branch"
        uniqueID = 1
        price = 4
        useable = False
        # equiping stats
        _type = "Weapon  "
        level = 1
        findLevel = 1
        hands = 1
        # life status
        health = 0
        stamina = 0
        # attack stats
        attack = 1
        strength = 1
        defense = 0
        protection = 0
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.basicItems.append(tempItem)
    #end Branch

    def addDagger(self):
        name = "Dagger          "
        # ends in 8... helps inventory
        desc = "A rusty dagger that is reasonably sharp and might be more useful than your fist"
        uniqueID = 2
        price = 10
        useable = False
        # equiping stats
        _type = "Weapon  "
        level = 1
        findLevel = 2
        hands = 1
        # life status
        health = 0
        stamina = 0
        # attack stats
        attack = 2
        strength = 2
        defense = 0
        protection = 0
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.basicItems.append(tempItem)
    #end Dagger

    # ---advanced---
    def addLongSword(self):
        name = "Long Sword      "
        desc = "A finely polished steel longsword. It gleans in the torchlight and is razor sharp."
        uniqueID = 101
        price = 100
        useable = True
        # equiping stats
        _type = "Weapon  "
        level = 1
        findLevel = 2
        hands = 1
        # life status
        health = 0
        stamina = 0
        # attack stats
        attack = 3
        strength = 10
        defense = 2
        protection = 0
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.advancedItems.append(tempItem)
    #end long sword

    # ---epic---
    def addClaymore(self):
        name = "Claymore       "
        # ends in 8... helps inventory
        desc = "A bright SHINY new sword"
        uniqueID = 201
        price = 600
        useable = False
        # equiping stats
        _type = "Weapon  "
        # ends in 8... helps inventory
        level = 1
        # what level the item is..
        findLevel = 4
        # what level you can find it on
        hands = 1
        # life status
        health = 0
        stamina = 1
        # attack stats
        attack = 3
        strength = 10
        defense = 3
        protection = 0
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.epicItems.append(tempItem)
    #end ClayMore

    def addFlamingSword(self):
        name = "Flaming Sword   "
        desc = """You pick up this sword and it bursts to flames like a furnace. Inside your head, you hear a voice saying, 
        Hello, my name is BURNINAOR. Would you like to toast some enemies?"""
        uniqueID = 202
        price = 800
        useable = True
        # equiping stats
        _type = "Weapon  "
        level = 1
        findLevel = 5
        hands = 1
        # life status
        health = 0
        stamina = 2
        # attack stats
        attack = 5
        strength = 20
        defense = 5
        protection = 0
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.epicItems.append(tempItem)
    #end flaming sword

    # ****Armor****
    # ---basic---
    def addLeatherArmor(self):
      name = "Leather Armor   "
      # ends in 8... helps inventory
      desc = "A dirty leather shirt with iron rivets sewn into. It will stop a blade better than your skin."
      uniqueID = 51
      price = 20
      useable = False
      # equiping stats
      _type = "body    "
      level = 1
      findLevel = 1
      hands = 0
      # life status
      health = 0
      stamina = 0
      # attack stats
      attack = 0
      strength = 0
      defense = 1
      protection = 2
      # speed stats
      speed = 0

      tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
      self.basicItems.append(tempItem)
    # end leather armor
    # ---advanced---
    def addIronArmor(self):
        name = "Iron Armor      "
        # ends in 8... helps inventory
        desc = "An old rusty iron chestplate that is still intact slightly."
        uniqueID = 52
        price = 30
        useable = False
        # equiping stats
        _type = "Armor   "
        level = 1
        findLevel = 3
        hands = 0
        # life status
        health = 0
        stamina = 0
        # attack stats
        attack = 0
        strength = 0
        defense = 4
        protection = 8
        # speed stats
        speed = 0

        tempItem = Item(name, desc, uniqueID, price, useable, _type, level, findLevel, hands, health, stamina, attack, strength, defense, protection, speed)
        self.basicItems.append(tempItem)
   #end Iron Armor
   # ---epic---

   # addSteal()

   # ****Misc****
   # ---basic---

   # ---advanced---

   # ---epic---
