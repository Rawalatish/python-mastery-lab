#     Multilevel Inheritance
class A:                                    # Parent Class
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B(A):                                  # Child of class A
    a, b  = 40, 30
    def m2(self):
        print(self.a - self.b)

class C(B):                                  # Child of class B
    m, n  = 50, 60
    def m3(self):
        print(self.m * self.n)

# Create object of class B

objb = B()

# Access m & v of Class B and A
print(objb.x)
print(objb.y)

print(objb.a)
print(objb.b)
print("====")
objb.m1()
objb.m2()
print("=====")
# Create object of class C

objc = C()

print(objc.m)
print(objc.a)
print(objc.x)

# Accessing the methods from class A, B and C
objc.m1()
objc.m2()
objc.m3()
