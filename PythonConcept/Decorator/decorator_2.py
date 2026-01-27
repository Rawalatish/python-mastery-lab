# nested function

def outer(x):
    def inner(y):
        return x -y
    return inner

substract_six = outer(10)
result = substract_six(6)

print(result)       # 4