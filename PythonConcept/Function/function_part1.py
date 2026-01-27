#     Function

def myfunc():  # function creation/ declaration
    print("hi, this is function")


print("hi, keep going")

#         invoking or calling the function
myfunc()  # op: hi, this is function


# Arguments / parameters

def std_name(name):
    print("hi", name)


std_name("Ram")


def std_info(age, id):
    print(age, id)


std_info(10, "tx01")

# Return values


def add(x,y):

    return x + y


total = add(5, 3)
print(total)

print(add(20, 40))

# return none in following case


def myfc():
    return


print(myfc())                  # op: None


def myfc1():
    a = 10
    b = 20


print(myfc1())                # op: None