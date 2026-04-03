from symtable import Class


class A:

    __x= 0
    __y = 20
    def m1(self):
        __p = 30
        print("m1 from A")

    def m2(self):
        __q = 40
        print("m2 from A")

    def m3(self):
        __r = 50
        print(__r)
        print(self.__x)
        print("m3 from A")


objA = A()
objA.m3()

#
# class B:
#     def m1(self):
#         print("m1 from B")
#
#
# class C (B,A):
#     def m3(self):
#         print("m3 from C")
#
#
# C().m1()

