from hero import Hero
from monster import Monster

#gets user input and returns a response
def prompt_usr(prompt, typ):
    if typ == "number":
        response = input(prompt)
        while not response.isnumeric():
            print("Try again: ")
            response = input(prompt)
        #print("Entering response {}".format(response))
        return int(response)
    elif typ == "string":
        response = input(prompt)
        while not response.isalpha():
            print("try again: ")
            response = input(prompt)
        #print("Entering response {}".format(response))
        return str(response)

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

    response = prompt_usr("Select(N)ew game or (C)ontinue: \t", "string")
    if(response == "C"):
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
        monster = Monster("Happy Friend")
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
