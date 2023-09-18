def greatest(no):
    l=[]
    great=0
    for x in range(no):
        # try:
            x=int(input(f"Enter your {x+1} number:\n"))
            l.append(x)
        # except ValueError:
        #     pass
    great=l[0]
    for i in range(1,no-1):
        if great<l[i]:
            great=l[i]
            

    print(f"The greatest number is {great}")    

no=int(input("Enter how many numbers you want to find the greatest from:\n"))
greatest(no)
