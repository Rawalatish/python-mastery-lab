def number_generator(n):
    for i in range(n):
        yield i

# Use the generator
my_generator = number_generator(5)

# Iterate over the values
for number in my_generator:
    print(number)  # Output: 0 1 2 3 4

# Or, get values one by one
my_generator = number_generator(3)
print(next(my_generator))  # Output: 0
print(next(my_generator))  # Output: 1
print(next(my_generator))  # Output: 2