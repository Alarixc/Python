def func(str1,str2):
    m = True
    str1 = list(str1)
    str2 = list(str2)

    for x in str1:
        for index, y in enumerate(str2):
            if x == y:
                str2.pop(index)
                break
        else:
            m = False

    if m and not str2:
        print("The strings are anagrams of each other!")
               
 

                    
                



str1=input("Enter your first string:\n")
str2=input("Enter your second string:\n")
func(str1,str2)
