#   Super Function : Access Parent Class method by using super function

class A:
    def m1(self):
        print(" we are inside in m1 method of class A")

class B(A):
    def m1(self):
        print(" we are inside in m1 method of class B")
        super().m1()                                                # Super () function usage


objb = B()
objb.m1()

print("============= next example =========")

class Parent:
    def __init__(self):
        print("Parent class constructor")

    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls the Parent's constructor
        print("Child class constructor")

    def greet(self):
        super().greet()  # Calls the Parent's greet method
        print("Hello from the Child class!")

    

# Creating an instance of Child
child_instance = Child()
child_instance.greet()




