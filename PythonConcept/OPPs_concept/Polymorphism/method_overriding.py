#               Method Overriding   - Variable overriding

class Shape:
    mavar = "Shapeparent"

class Circle(Shape):
    myvar = "Circleshape"

cirobj = Circle()
a = cirobj.myvar
print(a)                    # Circleshape


