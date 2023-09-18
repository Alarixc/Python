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
    def __add__(self,other):
        return ThreeDVector(self.icap+other.icap,self.jcap+other.jcap,self.kcap+other.kcap)
    def __mul__(self,other):
        return ThreeDVector(self.icap*other.icap,self.jcap*other.jcap,self.kcap*other.kcap)
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
    def __len__(self):
        return len((self.icap+self.jcap+self.kcap))
    # def __repr__(self,other):
    #     return f"{self.icap+other.icap}i+{self.jcap+other.jcap}j+{self.kcap+other.kcap}k"


two=TwoDVector(4,5)
three=ThreeDVector(7,8,9)
three1=ThreeDVector(9,10,11)
print("The 2D vector is {}".format(two))
print("The 3D vector is {}".format(three))
print("The addition of two vectors is {}".format(three+three1))
print("The multiplication of two vectors is {}".format(three*three1))
print("The length of the vector is {}".format(len(three)))


