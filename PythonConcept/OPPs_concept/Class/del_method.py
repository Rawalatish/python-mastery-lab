class Animal:
    def __init__(self):
        print(" Object is created")

    def __del__(self):
        print(" object is destroyed")


obj = Animal()

# Object Destroying by using del
del obj
