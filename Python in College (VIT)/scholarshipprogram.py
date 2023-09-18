p=int(input("Enter physics marks:\n"))
c=int(input("Enter chemistry marks:\n"))
m=int(input("Enter maths marks:\n"))
avg=(p+c+m)/3
while(True):
    try:
        graduate=input("Are you first graduate?Y/N")
        if graduate=='Y':
            if avg>98:
                print("You are eligible for scholarship!")
            else:
                print("You are not eligible for scholarship!")
            exit()
        elif graduate=='N' or avg<98:
            print("You are not eligible for scholarship!")
            exit()
        else:
            print("Invalid!")
    except ValueError:
        pass

