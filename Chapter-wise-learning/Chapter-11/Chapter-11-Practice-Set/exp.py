# class Vector2d:
#     pass

# def Vector2d__init__(self, i, j):
#     self.i = i
#     self.j = j

# v = Vector2d()
# Vector2d__init__(v,3, 5)
class X:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return X(self.value + other.value)
    def __str__(self):
        return f'{self.value}'
a = X(1)
b=X(2)
c=a+b
d=X(10)
print(c+d)
print(type(c))

