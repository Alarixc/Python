n=float(input("Enter amount in hand:\n"))
c=float(input("Enter price of one chocolate:\n"))
m=int(input("Enter num of wrapper for free chocolate:\n"))
p= n//c

f= p//m
print("Number of chocolates are {} ".format(int(p+f)))
