i=int(input("Enter the number whose multiplication table you want:\n"))
y=int(input("Enter the number till where you want the multiplication table to go:\n"))
x=0
while x<y:
    table= i*(x+1)
    print(f'{i} X {x+1}={table}')
    x+=1


