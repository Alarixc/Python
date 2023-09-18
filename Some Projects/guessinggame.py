import random
import time
start=time.time()
class Guess:
    def __init__(self,guess,randNo,GuessCount,x):
        self.guess=guess
        self.random=randNo
        self.GuessCount=GuessCount
        self.x=x
    def determine(self):
        print(self.random)
        while self.guess is not self.random :
            while True:
                if self.guess>=0 and self.guess<=100:
                    break
                else:
                    print("Invalid! Try again!")
                    self.guess=int(input("Enter a random number between 1 and 100:\n"))
            if self.random>self.guess:
                print("Guess a Higher number please")
            else:
                print("Guess a Lower number please") 
            self.GuessCount+=1     
            self.guess=int(input("Enter a random number between 1 and 100:\n"))
            if(self.GuessCount==5 and self.guess is not self.random):
                self.x=False
                break
            elif(self.GuessCount==5):
                break
            
            
        if(self.x==True):
            print("Congratulations,You have won!You guessed the right number {} in {} tries".format(self.random,self.GuessCount))
        else:
            print("You have lost! You were given {} chances and you couldn't guess the right number {}!".format(self.GuessCount,self.random))
    
    def highscore(self):
        if(self.x==True):
            
            with open("highscore.txt","r") as f:
                hiscore =f.read()

            if hiscore=='':
                with open("highscore.txt","w") as f:
                    hiscore=f.write(str(self.GuessCount))
                    print("Your high score is {}".format(self.GuessCount))
                    exit(f"Program took {time.time()-start} seconds")
            if self.GuessCount<int(hiscore):
                with open("highscore.txt","w") as f:
                    hiscore=f.write(str(self.GuessCount))
                    print("Your new high score is {}".format(self.GuessCount))
            else:
                print("Your score is {}.Your high score was {}.".format(self.GuessCount,hiscore))
            
        print(f"Program took {time.time()-start} seconds")

randNo=random.randint(0,100)
guess=int(input("Enter a random number betwenn 1 and 100:\n"))
GuessCount=1
x=True
Gue=Guess(guess,randNo,GuessCount,x)
Gue.determine()
Gue.highscore()

