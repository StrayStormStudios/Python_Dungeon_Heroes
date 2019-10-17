from hero import Hero
from prompts import prompt_usr

hero = None


def intro():
    #Display for Intro
    print("""
    ******----******----******
    Welcome to Dungeon Heroes!
    ******----******----******
    
    \^~~~~\\   )  (   /~~~~^/
     ) *** \\  {**}  / *** (
      ) *** \\_ ^^ _/ *** (
       ) ****   vv   **** (
        )_****      ****_(
          )*** m  m ***(
    """)

def create_character():
    #name = prompt_usr("Enter your hero's name: \t", "string")
    #char_class = prompt_usr("What class shall they be, a mighty (W)warrior or cunning (T)thief? \t", "string")
    #hero = Hero(name, char_class)
    hero = Hero("bill", "warrior")
    return hero
    
if __name__ == "__main__":
    intro()
    #load old game or start a new one
    #response = prompt_usr("Select(N)ew game or (C)ontinue: \t", "string")
    #if(response == "C"):
        #try:
            #hero = SaveGame.load("saveGame.txt")
            #print("File Loaded")
        #catch(FileNotFoundException e):
            #print("SaveGame not found")
            #createCharacter(g_input)
    #else:
        #print("********")
        #print("NEW GAME")
        #print("********")
        #Create a character
    hero = create_character()   # player chooses their player class
    hero.stats()               # tests player and shows us status

    #Main loop to play game
    print()
    game_is_running = True
    while(game_is_running):    
        print("Starting battle")
        hero.fight_monster()
        get_in = input("Play Again? Y or N: \t")
        #Check for Player Input
        if get_in.lower() == "n":
            game_is_running = False
        else:
            #resart to play again"""
            pass
