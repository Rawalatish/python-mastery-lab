# Method Overriding

class Shape:
    def draw(self):
        print(" This is the generic method in the parent class")

class Circle(Shape):
    def draw(self):
        print(" This is the circle draw method")


class Rectangle(Shape):
    def draw(self):
        print(" This is the rectangle draw method")


class Square(Shape):
    def draw(self):
        print(" This is the square draw method")


cirobj = Circle()
cirobj.draw()

recobj = Rectangle()
recobj.draw()

