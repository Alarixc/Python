import math

def square(n):
    sum = 0
    for i in range(1,n+1):
        sum += math.pow(i,2)
    return sum

print(int(square(4)))




  