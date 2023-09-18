
n=int(input("Enter the number where you want the multiplication tables to start from:\n"))
nend=int(input("Enter the number where you want the multiplication tables to end:\n"))
z=int(input("Enter the number till where you want the multiplication tables of the numbers to go:\n"))
with open("Multiply.txt","w") as f:


    for x in range(n,nend+1):
        for y in range(z):
            
            f.write(f"{x} X {y+1} = {x*(y+1)}") #print(f"{x} X {y+1} = {x*(y+1)}", file=f) ==>Alternatively.
            f.write("\n")

        f.write("\n")
