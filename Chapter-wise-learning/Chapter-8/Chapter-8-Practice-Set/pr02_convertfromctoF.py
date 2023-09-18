def convert(Temp):
    F=(Temp*9/5 + 32)
    return F

Temp=float(input("Enter the Temperature in Celsius:\n"))
print(f"The Temperature in Farenheit is {convert(Temp)}")
