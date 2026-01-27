#    local, class and global variables

i, j = 50, 20                       # Global variables
a, b = 111, 111                    # Global variable with same local variable name

class Myclass:

    x, y = 10, 20                  # Class variables

    def add(self, a, b):            # Local Variable
        # a = 5
        # b = 6                 if we define the variables inside the parameter then we don't need to define like this

        print(a+b)               # op:11   # accessing the Local variables
        print(self.x + self.y)    # op: 30  # accessing the Class variables, need to be use self keyword

        print(i + j)              # op: 70  # accessing the Global variables

#         If we have same global and local variables name

        print(globals()["a"] + globals()["b"])        # op: 222




mc = Myclass()
print(id(mc))                     # op: 1875320950896  memory location of object
mc.add(5, 6)

