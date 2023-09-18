import math
class Calculator:
    @staticmethod
    def greet():
        print("Hello User!")
    
    def square(self):
        return math.pow(self.a,2)
    def squareRoot(self):
        return math.sqrt(self.a)
    def cube(self):
        return math.pow(self.a,3)


num=Calculator()
Calculator.greet() #OR num.greet()
n=int(input("Enter the number you want:\n"))
num.a=n
num.square()
num.squareRoot()
num.cube()
print(f"The square of number {n} is {num.square()}")
print(f"The square root of number {n} is {num.squareRoot()}")
print(f"The cube of number {n} is {num.cube()}")

