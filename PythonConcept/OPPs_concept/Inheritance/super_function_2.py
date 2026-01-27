
# Super function use in when we have the same variables names at global, parent and child class and local state
a, b = 10, 20
class A:
    a, b = 30, 40        # class variables

class B(A):              # Class variables
    a, b = 50, 60
    def add(self, a, b):           # Local variables
        print(a + b)                             # 3,  local variable
        print(self.a + self.b)                   # 110, class variables of class B
        print(globals()['a'] + globals()['b'])   # 30, Global variables

        print(super().a + super().b)             # 70, Class variables of class A


objc =B()

objc.add(1,2)

