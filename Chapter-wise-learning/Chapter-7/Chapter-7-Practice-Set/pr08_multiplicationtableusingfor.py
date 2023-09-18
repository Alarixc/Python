n=int(input("Enter the number whose multiplication table you want:\n"))
y=int(input("Enter the number till where you want the multiplication table to go:\n"))
for x in range(0,y):
    # print(str(n)+ " X "+ str(x+1)+ "="+ str((x+1)*n))
    print(f"{n} X {x+1}= {(x+1)*n}")
    


