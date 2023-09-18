h=int(input("Enter the number of hours you wanna browse:\n"))
m=int(input("Enter the number of minutes you wanna browse for:\n"))
bill=h*50+m*1
if h>=5 and h<=7 and m>=0 and m<61:
    bill=200+(h-5)*50+m*1
elif h>7 or m>60 or m<0:
    print("Invalid Entry!")
    exit()

print("Your bill is",bill)


    