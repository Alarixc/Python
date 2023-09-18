content= True
i=1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print("Python is present at line {}".format(i))
        i+=1

    