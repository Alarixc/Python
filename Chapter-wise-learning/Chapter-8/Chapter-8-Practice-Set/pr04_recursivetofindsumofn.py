def func(n):
    if(n==0):
        return 0
    else:
        return n+func(n-1)
        



n=int(input("Enter the number:\n"))
print(f"The sum of {n} natural numbers is {func(n)}")
