# n=int(input("Enter the number of elements you want in your list:\n"))
l=[2,4,5,6,7,2,4,5,2]
# for x in range(n):
#    x=int(input()) 
#    l.append(x)

for index,x in enumerate(l):
    try:
        print(l[2*index+2])
    except Exception as e:
        pass

    



    