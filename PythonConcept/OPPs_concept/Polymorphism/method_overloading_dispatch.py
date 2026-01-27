#   Multiple Dispatch
from xmlrpc.client import Boolean

from multipledispatch import dispatch

class A:
    @dispatch(int)
    def add(self, a):
        print("int type, sinle para", a)

    @dispatch(int, int)
    def add(self,a, b):
        print("int type, double para", a + b)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print("int type, triple para", a + b +c)

    @dispatch(int, float)
    def add(self, a, b):
        print("int and float type, double para ", a + b)
    #
    # @dispatch(str, Boolean)
    # def add(self, a, b):
    #     print("str and Boolean type, double para", a + b)    # error throws because we use Boolean type

    @dispatch(str)
    def add(self, a):
        print("str type, single para", a )



myobj = A()

myobj.add(10)
myobj.add(10, 20)
myobj.add(10, 20, 30)
myobj.add(10, 20.5)
myobj.add("Overloading method")
