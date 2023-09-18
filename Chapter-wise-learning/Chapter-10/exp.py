prices = {"Strawberries" : 1.5, "Banana" : 0.5, "Mango" : 2.5,
        "Blueberries" : 1, "Raspberries" : 1, "Apple" : 1.75,
        "Pineapple" : 3.5}

class Beverage:

    def __init__(self,join):
        self.join = join
    
    def ingredient(self):
        return (self.join)

    def get_cost(self):
        global prices
        return prices[self.join]

s1=Beverage("Strawberries")
print(s1.get_cost())

