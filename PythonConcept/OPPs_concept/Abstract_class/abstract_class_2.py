#multiple abstract method in abstract class

from abc import ABC, abstractmethod

class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class Y(X):
    def m1(self):
        print("m1 method from abstract")

class Z(Y):
    def m2(self):
        print("m2 method from abstract")

myobj1 = Z()
myobj1.m1()
myobj1.m2()










