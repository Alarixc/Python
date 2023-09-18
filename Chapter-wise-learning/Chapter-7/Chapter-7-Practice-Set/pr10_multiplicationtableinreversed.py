num=int(input("Enter the number whose multiplication table you want:\n"))
endno=int(input("Enter the number till where you want the multiplication table of the number:\n"))
for i in range(endno,0,-1):
    table=num*(i)
    print(f"{num} X {i}= {table}")
    



