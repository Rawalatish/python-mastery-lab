# passing function as Argument

def multiply(x, y):
    return (x * y)

def add(x, y):
    return (x + y)

def calculation(func, x , y):
    return func(x, y)

result_multiply = calculation(multiply,10, 11)
print(result_multiply)          # 110

result_add = calculation(add,10, 10)
print(result_add)               # 20