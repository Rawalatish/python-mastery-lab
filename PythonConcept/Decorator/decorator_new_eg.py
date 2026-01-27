def dec1(func):
    def wrap1():
        print("dec1 before")
        func()
        print("dec1 after")
    return wrap1

def dec2(func):
    def wrap2():
        print("dec2 before")
        func()
        print("dec2 after")
    return wrap2

def dec3(func):
    def wrap3():
        print("dec3 before")
        func()
        print("dec3 after")
    return wrap3

@dec1
@dec2
@dec3
def greet():
    print("hello im main function")

greet()

