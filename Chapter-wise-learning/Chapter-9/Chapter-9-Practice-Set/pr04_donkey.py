import re
with open("Something.txt", "r") as f:
    a = f.read()
    print(a)
    a= re.sub("Something","#########",a,flags=re.IGNORECASE)
    
print(a)

# if you want to ignore whitespace between characters, then... hmm
# [22:30]
# technically it's the 4th argument, it's the number of times to apply the substitution
# replace has it too
# >>> 'aaaaa'.replace('a', 'b')
# 'bbbbb'
# >>> 'aaaaa'.replace('a', 'b', 2)
# 'bbaaa'
# i don't think i've ever used it and a lot of people probably don't know about it but it's there
    
    