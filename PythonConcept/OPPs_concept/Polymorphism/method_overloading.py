

# class A:
#     def add(self,a):
#         print(a)
#
#     def add(self, a, b):
#         print(a + b)
#
# obja = A()
#
# obja.add(5, 2)
# obja.add(5)                # it will throw the error

# To avoid this we can use overloading methods with different approach
# Approach 1:
class A:
    def add(self, a = None, b = None):
        if a != None and b == None:
            print(a)
        else:
            print(a + b)

myobj = A()
myobj.add(2)
myobj.add(5+8)
