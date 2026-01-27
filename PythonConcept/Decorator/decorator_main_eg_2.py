# Decorator with parameters

def smart_division(func):
    def inner(x, y):
        if y == 0:
            print(" opps can't divided by 0")
            return 
        func(x, y)
    return inner

@smart_division
def division(x, y):
    print(x/y)

division(10, 0)
