def pattern(n):
    for _ in range(1,n+1):
            print("*",end=" ")
    
    print()
        
    
    if n==1:
        return 1
    pattern(n-1)

x=int(input("Enter the number:\n"))
pattern(x)


