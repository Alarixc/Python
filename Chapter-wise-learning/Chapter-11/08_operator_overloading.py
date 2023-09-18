class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Add:")
        return self.num + num2.num    #n1 + n2 is equivalent to n1.__add__(n2)
                                       # "n1 + n2", python is calling the dunder add on n1 and passing n2 to it, both of which are number() instances

    def __mul__(self, num2):
        print("Multiply:")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)