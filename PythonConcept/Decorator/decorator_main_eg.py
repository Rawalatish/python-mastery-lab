
# Python Decorators

def extragreeting(func):
    def inner():
        print(" from inner function, hello")
        func()                              # original function simplegreeting
    return inner

def add_stars(func):
    def inner1():
        print(" *********")
        func()                          # original function simplegreeting
    return inner1

@add_stars
@extragreeting                        # this is similar to: simplegreeting = extragreeting(simplegreeting)
def simplegreeting():
    print(" Hello python")

def test():
    print("whereas")

simplegreeting()
test()

def test():
    print("hfjhfjdhf")