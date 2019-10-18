"""
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
   for(int i=0 i < basic i++):
      lootItems.append(g_loot.getBasic(hero))
   # setup the advanced items
   for(int i=0 i < advanced i++):
      lootItems.append(g_loot.getAdvanced(hero))
   # setup the epic items
   for(int i=0 i < epic i++):
      lootItems.append(g_loot.getEpic(hero))

   if(len(lootItems) > 0):
      # print a list of the items
      print()
      print("***************")
      print("Treasure Items")
      print("**************")
      for(Item i: lootItems){
         print(i.uniqueID + " " + i.name) }
      print()
      # ask the user whether they want to(S)ell items or (K)eep items
      valid_response = False
      response = ""
      while(not response == "S" and not response == "K"):
         response = prompt_usr("Do you want to (S)ell or (K)eep the items (duplicates will be added to your current weapons): \t","string")
      # sell
      if(response == "S"):
         for(Item i: lootItems):
               hero.gold += i.price / 10
         print("You wisely sell the items")
      else:
         # put items in inventory(upgrade if duplicate)
         for(Item i: lootItems):
               hero.gold +=  hero.inventory.add(i)
         print("      ____   ")
         print("  .--[[__]]---.   ")
         print(" .-----------.|   ")
         print(" |           ||   ")
         print(" |           ||   ")
         print(" |___________|/   ")
         print("You wisely put the items in your backpack.")

"""






