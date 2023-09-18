# n=int(input("Enter a number:\n"))
# for x in range(n):
#     print("*" * n)
#     for x in range(2,n+1):
#         print("*",2:n+1:n-2)
    
n = int(input())
# output = "*" * n + "\n" 
# for i in range(n - 2):
#   output += ("*" + " " * (n - 2) + "*")
#   output += "\n" 
# output += "*" * n
# print(output)

for row in range(n):
    for col in range(2*n):
       print('*' if row in(0,n-1) or col in(0,(2*n)-1) else ' ', end=' ')
    print()