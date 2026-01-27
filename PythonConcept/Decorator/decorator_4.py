# Return a function as a value

def greeting(name):
    def hello():
        return ("hello " + name)
    return hello()

greet = greeting("sham")
print(greet)
