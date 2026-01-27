

class Employee:
    empname = "sham"
    __empsalary = 50005

    def getsalary(self):
        print("Employee Salary: ", self.__empsalary)


    def setsalary(self, salary):

        if salary < 5000 or salary > 10000:
            print(" Salary is not in range")
        else:
            self.__empsalary = salary


myobj = Employee()

myobj.getsalary()

myobj.setsalary(60001)
myobj.getsalary()