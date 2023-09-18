class Employee:
    company="Microsoft"
    salary=5000
    salarybonus=500

    @property
    def salary1(self):
        return self.salary+self.salarybonus
    @salary1.setter
    def salaryIncrement(self,val):
        self.salary=val+self.salarybonus
        return self.salary

sal=Employee()
sal.salarybonus=6000
print("The salary is",sal.salaryIncrement)
