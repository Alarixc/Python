def multi(x,n):
    for i in range(x):
        print(f"{n} X {i+1}= {n*(i+1)}")

n=int(input("Enter the number:\n"))
x=int(input("Enter the number till where you want the multiplication table to go:\n"))
multi(x,n)



