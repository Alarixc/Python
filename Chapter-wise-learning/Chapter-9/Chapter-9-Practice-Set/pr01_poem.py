with open("Poem.txt","r") as f:
    a= f.read()
    print(a)
    if a.find("cunt")>=0:
        print("The word cunt exists in file.")
    else:
        print("The word cunt does not exist in file.")

