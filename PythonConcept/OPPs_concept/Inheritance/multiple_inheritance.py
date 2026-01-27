#     Multiple Inheritance

class A:                                            # Parent Class
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B:                                        # Parent Class
    a, b  = 40, 30
    def m2(self):
        print(self.a - self.b)

class C(A,B):                                         # Child Class
    m, n  = 50, 60
    def m3(self):
        print(self.m * self.n)


objc = C()

objc.m1()
objc.m2()
objc.m3()
print(objc.x, objc.a, objc.m)

