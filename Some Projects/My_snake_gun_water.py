import random

def game(Comp,player):
    if(Comp=='s' and player=='s' or Comp=='w' and player=='w' or Comp=='g' and player=='g'):
        return None
    if player=='w' and Comp=='s': 
        return False         
    elif player=='s' and Comp=='w':
        return True          
    elif player=='w' and Comp=='g':
        return True
    elif player=='g' and Comp=='w':
        return False
    elif player=='s' and Comp=='g':
        return False
    elif player=='g' and Comp=='s':
        return True
            

RandNo=random.randint(1,3)
if(RandNo==1):
    Comp='s'
elif(RandNo==2):
    Comp='w'
elif(RandNo==3):
    Comp='g'

player=input("Enter s for snake,g for gun or w for water contender!:\n")
game(Comp,player)
if game(Comp,player)==None:
    print("The game has come to a draw!")
elif game(Comp,player)==True:
    print("You have won!")
else:
    print("You have lost!")

print(f"You chose {player} and the Computer chose {Comp}!")




