class Animals:
    def animal(self):                                                                
        n=int(input("Enter the number of animals you want:\n"))
        animals=[]
        self.animals=animals
        self.num=n
        for x in range(n):
            x=input("Enter the name of Animal {}".format(x+1))
            animals.append(x)
        print(animals)
class Pets(Animals):
    def pets(self):
        self.animal()
        print(self.num)
        petanimals=[]
        num1=int(input("Enter the number of animals you want as pets:\n"))
        for x in range(num1):
                while(True):
                    x=input("Enter the animals you want as pets from the list:\n")
                    if(x in self.animals):
                        break
                    else:
                        print("Invalid!Try again!")
                if(x in self.animals):
                    self.animals.remove(x)
                    petanimals.append(x)
              
        print("The animals you didn't accept as pets are",*self.animals)
        print("Your pet animals are",*petanimals)

ani=Animals()
pet=Pets()
pet.pets()

    

