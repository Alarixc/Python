class Vector:
    def __init__(self,x,y,z):
        self.i=x
        self.j=y
        self.k=z

class PrintVector(Vector):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
    def __repr__(self):
        return (f"{self.i}i+{self.j}j+{self.k}k")


x=int(input("Enter the x dimension of vector:\n"))
y=int(input("Enter the y dimension of vector:\n"))
z=int(input("Enter the z dimension of vector:\n"))
vec=PrintVector(x,y,z)
print("The vector is {}".format(vec))


