n1=int(input("Enter number 1:\n"))
n2=int(input("Enter number 2:\n"))
n3=int(input("Enter number 3:\n"))
n4=int(input("Enter number 4:\n"))
a=0
if(n2>=n1):
    f1=n2
else:
    f1=n1
if(n3>=n4):
    f2=n3
else:
    f2=n4
if(f1>=f2):
    a=f1
else:
    a=f2

print("The greatest number is",a)
#OR USE max(a,b) function
print("The greatest number is",max(n1,n2,n3,n4))



    


