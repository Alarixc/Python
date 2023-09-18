import re
l=[]
n=int(input("Enter the number of elements you want in your list:\n"))
with open("Listofwords.txt","r") as f:
    a=f.read()
    print(a)
for x in range(n):
    x=input("Enter the word in the list that you wanna remove:\n")
    l.append(x)
print(*l)
with open("Listofwords.txt","r") as f:
    a=f.read()
    i=0
    for i in l:
        a= re.sub(i,"#",a,flags=re.IGNORECASE)
    print(a)
