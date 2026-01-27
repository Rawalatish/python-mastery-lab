class Parent:
    a = 10
    def __init__(self):
        print("Parent class constructor")

    def greet(self):
        print("Hello from the Parent class!")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls the Parent's constructor
        print("Child class constructor")

    def greet(self):
        super().greet()  # Calls the Parent's greet method             this way also we can access  Parent.greet(self)
        print("Hello from the Child class!")
        Parent.greet(self)


# Creating an instance of Child
child_instance = Child()
child_instance.greet()
