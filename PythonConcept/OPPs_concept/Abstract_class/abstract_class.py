
from abc import ABC, abstractmethod
class Fruit(ABC):
    @abstractmethod
    def color (self):
        pass

class Mango(Fruit):
    def color(self):
        print(" Mango is having yellow color")

class Cherry(Fruit):
    def color(self):
        print(" Cherry is having red color")

''' for abstract class we can not create object, but we can create object for subclasses/ child classes and we can 
call color method '''

obj1 = Mango()
obj1.color()

obj2 = Cherry()
obj2.color()



