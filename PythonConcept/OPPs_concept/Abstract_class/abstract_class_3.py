# Constructor in Abstract class

from abc import ABC, abstractmethod

class Calc(ABC):

    def __init__(self, num1, num2):
        self.num1 =num1
        self.num2 = num2

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

class X(Calc):

    def add(self):
        print(self.num1 + self. num2)

    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)


obj1 = X(15, 10)

obj1.add()
obj1.sub()
obj1.mul()