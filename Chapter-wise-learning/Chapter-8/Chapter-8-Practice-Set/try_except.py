def func(n):
    l=[]
    for x in range(n):
        try:
            x=int(input("Enter the number {}".format(x)))
            l.append(x)
        except ValueError:
            x=0
            pass

    print(l)


n=int(input("Enter the number of integers you want in your list:\n"))
func(n)
        