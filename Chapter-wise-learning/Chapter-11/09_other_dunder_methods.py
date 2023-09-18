class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    # def __str__(self):
    #     return f"Decimal Number: {self.num}"
    
    # def __len__(self):
    #     return 1

n = Number(9)
n1= Number(9)
sum=n1+n
print(type(n1+n))
print(sum)
# print(n)
# print(len(n))