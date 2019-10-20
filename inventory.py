from prompts import prompt_usr
from printables import Printables

class Inventory():
    # constructor
    def Inventory(self):
        itemList = dict()

    # add an item
    # returns the cost / 10 if they already have it
    def add(self, item):
        if(self.itemList.containsKey(item.uniqueID)):
            # if they already have the item... level it up
            # return item.price / 10 refund price
            i = self.itemList.get(item.uniqueID)
            item.attack += 2
            item.strength += 2
            item.defense += 2
            item.protection += 2
            item.price += item.price
            if(item.uniqueID >= 50 and item.uniqueID <= 100):
                item.speed -= 2
            
            print()
            print(item.name + " now sells for: $" + (item.price / 2))
            print(item.name + " now has: " + item.attack + " Attack")
            print(item.name + " now has: " + item.strength + " Strength")
            print(item.name + " now has: " + item.defense + " Defense")
            print(item.name + " now has: " + item.protection + " Protection")
            print(item.name + " now has: " + item.speed + " Speed")
            return 0
        else:
            # add the item
            self.itemList.put(item.uniqueID, item)
        return 0
    
    # checkInventory - -> Allows the user to check inventory and handle items
    def handleInventory(self, hero):
        response = ""
        while(not response == "C"):
            response = prompt_usr("Choose One: (L)list your items, E(x)amine an item, (S)ell an Item, (E)quip an item,"
                                  + "\n (U)unequip an item, or (C)lose backpack) \t", "string")
            # list items
            if(response == "L"):
                list_items()
            elif(response == "X"):
                examine(input)
            elif(response == "S"):
                hero.gold += remove()
            elif(response == "E"):
                equip(input, hero)
            elif(response == "U"):
                unequip(input, hero)
    
    # list - -> Lists the items in the inventory
    def list_items(self):
        # loop through inventory items
        print("\nItem Num\tName\tType\tLevel")
        print("****************************************")
        for item in self.itemList:
        #for(Map.Entry < Integer, Item > entry: itemList.entrySet()):
            # print the item number and value
            print("{} \t{} \t{} \t{}".format(item._id, item.name, item._type, item.level))
            #print(entry.getKey() + "\t" + entry.getValue().name + entry.getValue().type + entry.getValue().level)
            # print if the item is equipped or not
            if(item.equipped):
            # if(entry.getValue().equipped):
                print(" (Equipped)")
            
            print()
         # close for
     # close list

    # examines an item(prints the description)
    def examine_item(self, uniqueID):
        if(self.itemList.containsKey(uniqueID)):
            print()
            self.itemList.get(uniqueID).description()
        else :
            print("Unable to find object " + uniqueID)
    
    # prompts the user for an item to examine then examines it
    def examine(self):
        _id = prompt_usr("Which item would you like to examine (Enter the item number): ", "number")
        # parse the number(and catch)
        try :
            examine_item(_id)
        except ValueError:
            print("You must enter a valid number")
    
    # removes an item from the list based on its unique id and returns sell price / 10
    def remove_item(self, uniqueID):
        if(self.itemList.containsKey(uniqueID)):
            sellPrice = self.itemList.get(uniqueID).price / 10
            print("You sell the " + self.itemList.get(uniqueID).name + " for " + sellPrice + " gold.")
            Printables.print_money()
            self.itemList.remove(uniqueID)
            return sellPrice
        else:
            print("Unable to find object " + uniqueID)
            return 0
    
    # Prompts the user for an item to remove then removes it
    def remove(self):
        _id = prompt_usr("Which item would you like to remove (Enter the item number): ", "number")
        # parse the number(and catch)
        try:
            return remove_item(_id)  
        except ValueError:
            print("You must enter a valid number")
            return 0
    
    # equips an item from the list based on its unique id
    def equip_item(self, uniqueID, hero):
        # the item exists
        if(self.itemList.containsKey(uniqueID)):
            i = self.itemList.get(uniqueID)
            # if the item is equipped yell at user
            equippable = True
            if(i.equipped):
                print("The item is already equipped")
                equippable = False
            else:
                # if another item of the same type is equipped yell at user
                for item in self.itemList:
                #for(Map.Entry < Integer, Item > entry: itemList.entrySet()):
                    if (item._type == i.type) and item.equipped:
                    #if(entry.getValue().type == i.type) and entry.getValue().equipped):
                        print("You already have " + i.name + "of type " + i.type + ". Remove it first.")
                        equippable = False
                
                # if the user doesn't have enough hands... yell at user
                if(i.hands > hero.hands):
                    print("You don't have enough hands remaining to use that object")
                    equippable = False
                
                # equip the item
                if(equippable):
                    print("You equip the " + i.name)
                    i.equipped = True
                    hero.hands -= i.hands
                    hero.maxHealth += i.health
                    hero.maxStamina += i.stamina
                    hero.attack += i.attack
                    print("You no have: " + hero.attack + " Attack")
                    hero.strength += i.strength
                    print("You no have: " + hero.strength + " Strength")
                    hero.defense += i.defense
                    print("You no have: " + hero.defense + " Defense")
                    hero.protection += i.protection
                    print("You no have: " + hero.protection + " Protection")
                    hero.speed += i.speed
        else :
            print("Unable to find object " + uniqueID)
    
    # Prompts the user for an item to equip
    def equip(self, hero):
        _id = prompt_usr("Which item would you like to equip (Enter the item number): ", "number")
        # parse the number(and catch)
        try :
            self.equip_item(_id, hero)
        except ValueError:
            print("You must enter a valid number")
    
    # unequips an item from the list based on its unique id
    def unequip_item(self, uniqueID, hero):
        # the item exists
        if(self.itemList.containsKey(uniqueID)):
            i = self.itemList.get(uniqueID)
            # if the item is not equipped yell at user
            unequippable = True
            if(not i.equipped):
                print("The item is already unequipped")
            else:
                # unequip the item
                print("You remove the " + i.name)
                i.equipped = False
                hero.hands += i.hands
                hero.maxHealth -= i.health
                hero.health = min(hero.health, hero.max_health)
                hero.maxStamina -= i.stamina
                hero.stamina = min(hero.stamina, hero.max_stamina)
                hero.attack -= i.attack
                print("You now have: " + hero.attack + " Attack")
                hero.strength -= i.strength
                print("You now have: " + hero.strength + " Strength")
                hero.defense -= i.defense
                print("You now have: " + hero.defense + " Defense")
                hero.protection -= i.protection
                print("You now have: " + hero.protection + " Protection")
                hero.speed -= i.speed 
        else:
            print("Unable to find object " + uniqueID)
    
    # Prompts the user for an item to unequip
    def unequip(self, hero):
        _id = prompt_usr("Which item would you like to unequip (Enter the item number): ", "number")
        # parse the number(and catch)
        try :
            self.unequip_item(_id, hero) 
        except ValueError:
            print("You must enter a valid number")
