with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'r+') as f:
    a = f.write("me")

print(a)



