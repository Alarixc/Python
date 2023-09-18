def convert(inches):
    Cm=inches/2.54
    return Cm

inches=float(input("Enter the length in inches:\n"))
print(f"The length in centimeters is {convert(inches)}")
