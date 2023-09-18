x=int(input("Enter a number:\n"))
i=2
y=False
while(i<x):
    num=x%i
    if(num==0):
        y=True
        break  
    i+=1
    
if(y==True):
    print(f"The number {x} is not a prime number")
else:
    print(f"The number {x} is a prime number")

