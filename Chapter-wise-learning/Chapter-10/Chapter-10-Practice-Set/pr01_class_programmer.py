class Programmer:
    company="Microsoft"
    def details(self):
        print(f"The name of Programmer is {self.name} and programming language is {self.language}")
    

harry=Programmer()
george=Programmer()
harry.name="Harry Styles"
george.name="George Costanza"
harry.language="C"
george.language="Python"
harry.details()
george.details()
