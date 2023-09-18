class TwoDVector:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}k"

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"



two=TwoDVector(4,5)
three=ThreeDVector(7,8,9)
print("The 2D vector is {}".format(two))
print("The 3D vector is {}".format(three))

# super() is an object referring to the master class, already registered with the base class, in your case, you were passing self as the value of i and j because i, because you specified self, but self is basically you resending the object to thee super() object already linked to the base
