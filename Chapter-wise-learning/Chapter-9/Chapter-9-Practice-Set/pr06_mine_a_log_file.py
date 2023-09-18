with open("log.txt") as f:
    content=f.read()

if 'python' in content.casefold():  #OR content.lower()
    print("Python is present in log file")
else:
    print("Python is not present in log file")