from sty import fg, bg, ef, rs, RgbFg
from printables import print_case, print_chest
from save_game import save, load
from prompts import prompt_usr
from hero import Hero
from loot import Loot
import random
import time
import os

#chances of getting different rooms
#0-70  monster
#71-81 store
#82-90 1d4 basic treasures
#91-92 1d2 advanced treasures
#93  1 epic treasure(unguarded)
#94-99 exit
MONSTER_CHANCE = 0
#60 % chance of fighting a monster
#public static final int DARK_ROOM_CHANCE = 60
#(10 % chance) we come to a dark room..
#public static final int TRAP_ROOM_CHANCE = 80
#(5 % chance) we come to a dark room..
BASIC_TREASURE_CHANCE = 85
#(5 % chance) 1-2 basic items
ADVANCED_TREASURE_CHANCE = 90
#(3 % chance) 1-2 advanced items
EPIC_TREASURE_CHANCE = 93
#(6 % chance)1-2 epic treasure chest
EXIT_CHANCE = 99
# 1 percent of the time we reach exit
hero = None
loot = Loot()

def intro():
    #Display for Intro
    print(fg.green, bg.black +"""
    ******----******----******
    Welcome to Dungeon Heroes!
    ******----******----******""" + fg.red + """
    \^~~~~\\   )  (   /~~~~^/  
     ) *** \\  {**}  / *** (   
      ) *** \\_ ^^ _/ *** (    
      ) ****   vv   **** (    
       )_****      ****_(     
         )*** m  m ***(      """ + fg.rs, bg.rs)
    
def load_game():
    response = prompt_usr("Select (N)ew game or (C)ontinue: \t", "string").upper()
    if(response == "C"):
        try:
            hero = load("saveGame.txt")
            hero.stats()
            #print("File Loaded")
        except FileNotFoundError:
            print("SaveGame not found")
            create_character()
        #hero = Hero("bill", "warrior")
        return hero
    elif(response == "N"):
        hero = restart()
        print("\nThree months ago, you set out from your village looking for glory and riches.")
        print("After a long journey into the mountains, you came across a cave.")
        print("You hear horrible noises coming from inside.")
        response = prompt_usr(
            "Do you want to (E)enter or (L)leave? \t", "string").upper()
        if (response == "E"):
            return hero
        else:
            print("You Left")
            return
    else:
        print("Not an option, Sorry")
        print("Terminating")

def play(hero):
    #Main loop to play game
    if hero != None:
        game_is_running = True
    else:
        game_is_running = False
    while(game_is_running):
        #print("Starting battle")
        #hero.fight_monster()
        game_is_running = enter_room()

def play_again():
    play = prompt_usr("Play Again? Y or N: \t", "string").upper()
    if play == "N":
        print("Fine")
        time.sleep(2)
        print("bye bye")
    elif play == "Y":
        #resart to play again
        return restart()
    else:
        print("!!!What!!!\n\n")
        time.sleep(2)
        print("Nah Forget it, bye")

def restart():
    print("********")
    print("NEW GAME")
    print("********\n")
    hero = create_character()   # player chooses their player class
    hero.stats()               # tests player and shows us status
    return hero

def create_character():
    name = prompt_usr("Enter your hero's name: \t", "string")
    char_class = prompt_usr(
        "What class shall they be, a mighty (W)warrior or cunning (T)thief? \t", "string")
    hero = Hero(name, char_class)
    return hero

#enterRoom: enters a new room where the player will battle a monster etc
#@param --> input A scanner to console input
#@return --> False - stop playing the game, True - keep playing the game (enter a new room
def enter_room():
    print()
    print("***************************")
    print("You have entered a new room")
    treasure = 0
    
    levelUp = False
    
    if(hero.level == 4 or hero.level == 8 or hero.level == 12):
        if(hero.xp == 0):
            print()
            treasure = random.randint()*2 + 1 * 1 #1 or 2
            #self.getlevelUp(treasure)
            levelUp = False
    
    #get our random room
    room_type = random.random()*100# 0.0 --> 99.9999
    #are we at the end of the dungeon?
    #if(room_type >= EXIT_CHANCE):
    #   return exitRoom(g_input)
    
    #is this an epic chest
    if(room_type >= EPIC_TREASURE_CHANCE):
        print("$$$EPIC TREASURE ROOM$$$")
        print_chest()
        treasure = random.randint()*2 + 1 * 100 #100 or 200
    
    #is this an advanced treasure room?
    elif(room_type >= ADVANCED_TREASURE_CHANCE):
        print("$$$Advanced Treasure Room$$")
        print_chest()
        treasure = random.randint()*2 + 1 * 10 #10 or 20
    
    #is this a basic treasure room?
    elif(room_type >= BASIC_TREASURE_CHANCE):
        print("Basic Treasure Room!")
        print_chest()
        treasure = random.randint()*2 + 1 * 1 #1 or 2
    
    #otherwise we fight a monster.
    else:
        treasure = hero.fight_monster()
        if(treasure == -1):
            return False  #they have died... game over
        
    #gives the player randomly rolled treasure
    get_treasure(treasure)
    
    #handle Choosing whats next
    return choice()

#choice: allows the user to(E)enter next room, (R)est, (S)status or open(I)inventory, (Q)quit game
#@param - -> input A scanner to console input
#@return - -> True when they hit enter... False to leave the game
def choice():
    # prompt user
    print("\nThe room is now safe")
    response = ""
    while(not response == "E"):
        response = prompt_usr("Do you want to (R)est to recover stamina and health, check your(S)status, open your (I)inventory, " +
                              " \n(E)enter the next room, Enter the s(H)op, or save and (Q)uit the game. \t", "string").upper()
        # resting
        if(response == "R"):
            hero.rest()

        # status
        elif(response == "S"):
            hero.stats()

        # open inventory
        elif(response == "I"):
            hero.inventory.handleInventory(hero)

        #elif(response == "H"):
        #    g_store.enterStore(hero)

        # quit game
        elif(response == "Q"):
            #return False
            try:
                save(hero, r"save_game.txt")
                return False
            except FileNotFoundError:
                print("There was a problem Saving, file not found")
                return False
        return True

#getTreasure - rolls random treasure and allows the user to take it(or convert to money)
#@param int treasure(1s are basic, 10s are advanced, 100s are epic treasure)
def get_treasure(treasure):
    # build a list of items that dropped
    lootItems = []
    # number of basic items
    basic = treasure % 10
    # advanced items
    advanced = treasure / 10 % 10
    # epic items
    epic = treasure / 100 % 10
    # setup the basic items
    for i in range(basic):
        lootItems.append(loot.getBasic(hero))
    # setup the advanced items
    for i in range(advanced):
        lootItems.append(loot.getAdvanced(hero))
    # setup the epic items
    for i in range(epic):
        lootItems.append(loot.getEpic(hero))

    if(len(lootItems) > 0):
        # print a list of the items
        print()
        print("***************")
        print("Treasure Items")
        print("**************")
        for i in lootItems:
            print("{} {}\n".format(i.uniqueID, i.name))
        # ask the user whether they want to(S)ell items or (K)eep items
        valid_response = False
        response = ""
        while(not response == "S" and not response == "K"):
            response = prompt_usr(
                "Do you want to (S)ell or (K)eep the items (duplicates will be added to your current weapons): \t", "string")
        # sell
        if(response == "S"):
            for i in lootItems:
                hero.gold += i.price / 10
                print("You wisely sell the items")
    else:
        # put items in inventory(upgrade if duplicate)
        for i in lootItems:
            hero.gold += hero.inventory.append(i)
        print_case()
        print("You wisely put the items in your backpack.")

if __name__ == "__main__":
    #Print a cool intro
    intro()
    #Load old game or start a new one
    hero = load_game()
    #Main loop to play game
    play(hero)
    #Ask to play again
    play_again()
