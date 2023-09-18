password=input()
bool_l=[False,False,False,False]
l_alpha=[chr(i) for i in range(97,123)]
l_digit=[chr(i) for i in range(48,58)]
l_special=[chr(i) for i in [*range(32,48),*range(58,65),*range(91,97),*range(123,127)]]
if len(password)>=8:
    bool_l[0]=True
for i in l_alpha:
    if password.startswith(i) or password.startswith(i.upper()):
        bool_l[1]=True
        
for x in password:
    if x in l_digit:
        bool_l[2]=True
for z in password:
    if z in l_special:
        bool_l[3]=True

for element in bool_l:
    if element==False:
        print("Invalid")
        break
else:
    print("Valid")

