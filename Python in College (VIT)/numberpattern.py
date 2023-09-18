rows=int(input("Enter the number of rows you want:\n"))
i=0
for x in range(rows+1):
    for i in range(x):
        print(i+1,end="")
    print()


