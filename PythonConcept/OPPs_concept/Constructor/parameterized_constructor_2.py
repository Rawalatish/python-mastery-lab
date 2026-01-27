
class Employee:

    def __init__(self, empname, empid, empsalary):              # local variable and its in constructor so we make them class variable

        # here we are making local variable to Class variable by using self.variable name =variable name
        self.empname = empname
        self.empid = empid
        self.empsalary = empsalary

    def display(self):
        print(" Employee name is :", self.empname)
        print(" Employee id is :", self.empid)
        print(" Employee salary is :", self.empsalary)


# object creation

emp1 = Employee("ram", 1,12000)
emp1.display()

emp2 = Employee("sham",2, 15000 )
emp2.display()




