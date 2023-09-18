
while True:
    try:
        a=int(input("Enter the integer you want to divide the other integer from:\n"))
        b=int(input("Enter the integer you want to divide the other integer from:\n"))
        divide=a/b
        print(divide)
        break
    except ZeroDivisionError as e:
        print("Infinite")
        break
    except Exception as e:
        print(e)
        print("Make sure you enter a valid value")
