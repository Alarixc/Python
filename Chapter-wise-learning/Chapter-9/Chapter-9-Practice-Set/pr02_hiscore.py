def game():
    return 67


score = game()
with open("hiscore.txt") as f:
    aStr = f.read()

with open("hiscore.txt","w") as f:
    if(aStr==''):
        f.write(str(score))
    elif(int(aStr)>score):
        f.write(str(score))
    else:
        f.write(str(score))
    