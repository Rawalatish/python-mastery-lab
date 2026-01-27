#     Single Inheritance
class A:
    x, y = 10, 20
    def m1(self):
        self.total= self.x + self.y
        print("from m1 method" ,self.total)

class B(A):
    a, b  = 40, 30
    def m2(self):
        print(self.a - self.b)

obj = B()
# Accessing variables from class B and A
print(obj.a)
print(obj.b)
print(obj.x)


# Accessing the methods from class B and A
obj.m1()
obj.m2()

print(obj.total)