with open("hello.txt") as f:
    content=f.read()

with open("hello1.txt") as f:
    content1=f.read()

if content==content1:
    print("The contents of both the files are same")
else:
    print("The contents of both the files are not same")