def rem(n):
    l=[]
    for x in range(n):
        x=input(f"Enter element {x+1} of list:\n")
        l.append(x)

    print(l)
    while(True):
        y=input("Do you wanna remove any word from the list?Y/N\n")
        if(y=='Y'):
            z=input("Enter the word that you wanna remove from your list:\n")
            while z in l:
                l.remove(z)
                z.strip()
            print(l)
        elif(y=='N'):
            exit()
        else:
            print("Invalid!")
            # exit()

n=int(input("Enter the number of elements you want in your list:\n"))
rem(n)

