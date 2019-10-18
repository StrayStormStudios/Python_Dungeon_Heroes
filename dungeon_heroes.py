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
    name = prompt_usr("Enter your hero's name: \t", "string")
    char_class = prompt_usr("What class shall they be, a mighty (W)warrior or cunning (T)thief? \t", "string")
    hero = Hero(name, char_class)
    return hero

def restart():
    print("********")
    print("NEW GAME")
    print("********\n")
    hero = create_character()   # player chooses their player class
    hero.stats()               # tests player and shows us status
    return hero

def load_game():
    response = prompt_usr("Select (N)ew game or (C)ontinue: \t", "string").upper()
    if(response == "C"):
        #try:
            #hero = SaveGame.load("saveGame.txt")
            #print("File Loaded")
        #catch(FileNotFoundException e):
            #print("SaveGame not found")
            #createCharacter(g_input)
        hero = Hero("bill", "warrior")
        return hero
    elif(response == "N"):
        hero = restart()
        print("\nThree months ago, you set out from your village looking for glory and riches.")
        print("After a long journey into the mountains, you came across a cave.")
        print("You hear horrible noises coming from inside.")
        response = prompt_usr("Do you want to (E)enter or (L)leave? \t", "string").upper()
        if (response == "E"):
            return hero
        else:
            print("You Left")
            return
    else:
        print("Not an option, Sorry")
        print("Terminating")

if __name__ == "__main__":
    intro()
    
    #load old game or start a new one
    hero = load_game()

    #Main loop to play game
    print()
    game_is_running = True
    while(game_is_running):
        #print("Starting battle")
        if hero != None:
            hero.fight_monster()
        
        play = prompt_usr("Play Again? Y or N: \t", "string").upper()
        if play == "N":
            game_is_running = False
        else:
            #resart to play again
            hero = restart()
            pass
