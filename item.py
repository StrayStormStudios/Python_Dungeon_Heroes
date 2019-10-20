#Item class - -> keeps track of items
class Item():
    #Constructor
    def __init__(self, name, desc, uniqueID, price, useable, _type, level, findLevel, hands, 
                health, stamina, attack, strength, defense, protection, speed):
        #description stats
        self.name = name
        self.desc = desc
        self.uniqueID = uniqueID
        self.price = price
        self.useable = useable
        #equiping stats
        self.type = _type
        self.level = level
        self.findLevel = findLevel
        self.hands = hands
        self.equipped = False
        #life stats
        self.health = health
        self.stamina = stamina
        #attack stats
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.protection = protection
        #speed stats
        self.speed = speed

    #description - -> Describes the current item to the user
    def __repr__(self):
        print("**************** " + self.name + " ****************")
        print("* Description: " + self.desc)
        print("* Price: " + self.price)
        print("* Type: " + self.type)
        print("* Useable: " + self.useable)
        print("* level: " + self.level)
        print("* level unlocked on: " + self.findLevel)
        if self.hands > 0:
            print("* Hands: " + self.hands)
        if self.health != 0:
            print("* Health: " + self.health)
        if self.stamina != 0:
            print("* Stamina: " + self.stamina)
        if self.attack != 0:
            print("* Attack: " + self.attack)
        if self.strength != 0:
            print("* Strength: " + self.strength)
        if self.defense != 0:
            print("* Defense: " + self.defense)
        if self.protection != 0:
            print("* Protection: " + self.protection)
        if self.speed != 0:
            print("* Speed: " + self.speed)
        print("************************************************")
