# x=int(input("Enter the number whose factorial you want:\n"))
# y=x
# factorial=1
# while(y>=1):
#     factorial=factorial*y
#     y-=1

# print(f"The factorial of {x} is {factorial}")

num=int(input("Enter the number whose factorial you want:\n"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The factorial of {num} is {factorial}")
