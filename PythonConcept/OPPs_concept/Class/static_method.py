class MyClass:
        # Instance method
    def m1(self):
        print("inside the m1 method")

        # Static method
    @staticmethod
    def m2():
        print(" inside the m2 method")


p1 = MyClass()
p1.m1()

# We can call static method directly by using class name we don't need object for callling  static method

MyClass.m2()