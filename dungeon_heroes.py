from hero import Hero

if __name__ == "__main__":
    #Intro
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
    
    print("Select (N)ew game or (C)ontinue")
    response = getResponse()
    if(response.equals("C")):
        pass
        #try:
            #g_player = SaveGame.load("saveGame.txt")
            #print("File Loaded")
        #catch(FileNotFoundException e):
            #print("SaveGame not found")
            #createCharacter(g_input)
    else:
        print("********")
        print("NEW GAME")
        print("********")
        #Create a character
        hero = Hero("SandBoi", "Warrior")
        #createCharacter(g_input) # player chooses their player class
        #g_player.status() # tests player and shows us status


    #Main loop to play game
    print()
    game_is_running = True
    while(game_is_running):
        print("Starting battle")
        get_in = input("Play Again? Y or N: \t")

        #Check for Player Input
        if get_in.lower() == "n":
            game_is_running = False
        else:
            #resart to play again
            pass
"""
boolean playGame = true
    #starting room
    if(startRoom(g_input).equals("L")):
        playGame = false
    while(playGame):
        playGame = enterRoom(g_input); # Keep playing until the user quits

"""
