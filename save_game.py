from hero import Hero
from loot import Loot

#saves a player
def save(hero, file_name):
    try:
        save = open(file_name, "w")
        # save the player name
        save.write(hero.name)
        # save the playerClass
        save.write(hero.characterClass)
        # save the level
        save.write(hero.level)
        # save the experience
        save.write(hero.xp)
        # save the food
        save.write(hero.food)
        # save the gold
        save.write(hero.gold)
        # save a list of the items
        for item in hero.inventory.itemList:
        #for(Map.Entry < Integer, Item > entry: hero.inventory.itemList.entrySet()):
            save.write(item + " ")
        save.write()
        # save a list of the equipped items
        for item in hero.inventory.itemList:
        # for(Map.Entry < Integer, Item > entry: hero.inventory.itemList.entrySet()):
            if item.equipped:
            #if(entry.getValue().equipped){
                save.write(item + " ")
        save.close()
    except FileNotFoundError as error:
        #print(error)
        print("File not found")

def load(file_name):
    try:
        load = open(file_name)
        # read the player name
        name = load.readline()
        # read the player class
        character_class = load.readline()
        # make the player
        hero = Hero(name, character_class)
        # Load  the level
        level = int(load.readline())
        for i in range(level):
            hero.giveXP(10000)
        # load the current xp
        xp = int(load.readline())
        hero.giveXP(xp)
        # load the food
        food = int(load.readline())
        hero.giveFood(food)
        # load the gold
        gold = int(load.readline())
        hero.giveGold(gold)

        # Initialize a loot list
        loot = Loot()
        
        # Get a list of items add them to the player's inventory
        item_string = ""
        load.readline()
        if(load.hasNextLine()):
            item_string = load.readline()
        """
        Scanner items = new Scanner(itemString)
        while(items.hasNextInt()):
            uniqueID = items.nextInt()
            hero.inventory.add(loot.getItem(uniqueID))
        
        # equip items
        String equippedString = ""
        if(input.hasNextLine()):
            equippedString = input.nextLine()
        
        Scanner equipped = new Scanner(equippedString)
        while(equipped.hasNextInt()):
            uniqueID = equipped.nextInt()
            hero.inventory.equip(uniqueID, hero)
        
        hero.inventory.list()
        
        return hero
        """
    except FileNotFoundError:
        print("File Not Found")
        #throw new FileNotFoundException()
