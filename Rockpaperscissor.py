import random 
print("welcome to stone|paper|scissors")
play=input("enter 1 to play")
def select_menu():
    print("enter 1 to select stone")
    print("enter 2 to select paper")
    print("enter 3 to select scissor")
   
 
upoints=0
cpoints=0    
choice=True
while(choice):
      
      
      select_menu()
      ch= int(input("User turn: "))
      if ch==1:
          print("you chose stone")
      elif ch==2:
          print("you chose paper")
      elif ch==3:
          print("you chose scissor")
      else:
          print("enter a valid choice")
          continue

      print("\nNow its computer turn.......")

      comp_choice = random.randint(1, 3)
      if comp_choice == 1:
          print("I chose stone")
        
      elif comp_choice == 2: 
          print("I chose paper")
      else: 
          print("I chose scissor")
          
          
      
      if((ch == 1 and comp_choice == 3) or (ch == 2 and comp_choice ==1 ) or (ch==3 and comp_choice==2)):
          print("uggh!! I lost")
          upoints=upoints+1
          print("upoints is: ",upoints)
  
          
      elif((ch == 3 and comp_choice == 1) or (ch == 1 and comp_choice == 2) or (ch==2 and comp_choice==3)):
          print("Yes!! I win this round")
          cpoints=cpoints+1
          print("cpoints is: ",cpoints)
         

      elif((ch == 1 and comp_choice == 1) or (ch == 2 and comp_choice ==2 ) or (ch==3 and comp_choice==3)):
          print("Its a tie,lets try again")
      else: 
          print("Lets try again")
          


      if (upoints>=5):
          print("You won this match,I will see u next time")
      elif(cpoints>=5):
          print("Yippie,whos your daddy now")
      else:
          print("we still have a game to play")
          
          print("Do you want to play again? (Y/N)")
          
          ans = input()
          if ans == 'n' or ans == 'N':
              break
          print("\nThanks for playing")


   
