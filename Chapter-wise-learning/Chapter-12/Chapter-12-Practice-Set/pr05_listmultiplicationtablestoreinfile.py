n=int(input("Enter the number whose multiplication table you want:\n"))
l=[n*(i+1) for i in range(10)]
with open("Multiplication Table.txt","a") as f:
    for x in l:
        f.write(f"{x}\n")

print(l)

