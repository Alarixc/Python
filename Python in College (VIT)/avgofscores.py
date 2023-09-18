def func():
    l=[]
    for x in range(4):
        x=int(input(f"Enter your {x+1} score:"))
        l.append(x)
    sum=0
    for i in range(4):
        sum+=l[i]
    avg=sum/4
    print("The average of your 4 scores is {}".format(avg))


func()


    
