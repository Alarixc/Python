a=int(input("Enter marks of Physics:\n"))
b=int(input("Enter marks of C language:\n"))
c=int(input("Enter marks of Python language:\n"))
total=(a+b+c)/3
if(a<33 or b<33 or c<33 or total<40):
    print("You have failed!")
else:
    print("You have passed!")




