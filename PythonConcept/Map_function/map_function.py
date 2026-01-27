
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x


squared_numbers = map(square, numbers)  # Returns a map object

squared_numbers_list = list(squared_numbers) # Convert to a list to see the results

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]