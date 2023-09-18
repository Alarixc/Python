file1=input("Enter the file that you wanna open:\n")
while(True):
    try:
        with open(file1,"r") as f:
            content=f.read()
            print(content)
            break
    except Exception as e:
        print(e)
        file1 =input('Please ensure that you are opening a file that exists:')
