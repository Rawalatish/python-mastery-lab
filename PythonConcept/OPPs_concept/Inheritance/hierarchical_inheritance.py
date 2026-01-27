#     Hierarchical Inheritance

class A:                                            # Parent Class A
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B(A):                                        # Child of Class A
    a, b  = 40, 30
    def m2(self):
        print(self.a - self.b)

class C(A):                                         # Child of Class A
    m, n  = 50, 60
    def m3(self):
        print(self.m * self.n)


# class B object creation, and it only accesses class A and B, m & v
objb = B()
objb.m2()
objb.m1()
# objb.m3()                    # op: Attribute error while accessing Class C, m & v

# class C object creation, and it only accesses class A and C, m & v
objc = C()
print(objc.x)
print(objc.n)
objc.m3()


