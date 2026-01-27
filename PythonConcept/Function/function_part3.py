def myfunc(x, y, z):
    print(x, y, z)


# myfunc(1, 2 , 3)      # positional args
myfunc(x= 11, z= 33, y= 22)

# Default Parameter value


def myfc1(name, country = "India"):
    print(name, country)

myfc1("Ram")                  # op: Ram India

# Combination of positional and keyword arguments

def myfc2(a, b, c):
    print(a, b, c)


myfc2(10, 20, 30)      # positional args  : valid
myfc2(a=10, b=20, c=30)         # keyword args : valid
myfc2(c=30, a=10, b=20)         # keyword args : valid
myfc2(10, 20, c=30)       # combination of positional and keyword args : valid
# myfc2(10, b=20, 30)          # Invalid, after keyword arg we can not define positional args


# Arbitrory Arguments, *args

def myfc3(*kids):
    print(kids)
    print(kids[1])


myfc3("ram", "sham", "sita")

