#   global and local variables

myvar1 = 200  # global variable


def myfunc():
    myvar2 = 2  # local variable
    print(myvar2)
    print(myvar1)


myfunc()                       #op: 2 and 200

print(myvar1)                   # op: 200
# print(myvar2)                   # op: name error through because we are trying to access local var outside the function


# global variable inside the function
abc = 1111
def myfc1():
    global abc
    abc = 222
    print(abc)


myfc1()                 # op : 222
print(abc)              # op : 222
