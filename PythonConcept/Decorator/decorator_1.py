# nested function

def my_decorator(func):
    def wrapper():
        # Code to execute before the original function
        print("Before function call")

        func()  # Call the original function

        # Code to execute after the original function
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()