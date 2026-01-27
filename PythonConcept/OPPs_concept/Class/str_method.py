class MyClass:
    pass

myobj = MyClass()
print(myobj)                     # op: memory address of the the object in the string format

# ==========================
print("================")

class MyClass2:
    def __str__(self):
        return ("Hello world")               # it will always return string

myobj = MyClass2()
print(myobj)

# ================================
print("=============")

class MyClass3:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print(" emp name is {} empid is {} empsalary is {}".format(self.name, self.id, self.salary))


emp1 = MyClass3("rama", 1, 1200)
emp1.display()

''' so here we can use str() method also instead of display '''
# ==================
print("=========")

class MyClass4:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self):
        return (" emp name is {} empid is {} empsalary is {}".format(self.name, self.id, self.salary))


emp2 = MyClass4("sham", 11, 1500)
print(emp2)
