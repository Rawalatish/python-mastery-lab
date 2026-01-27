even_number = [2, 4, 6, 7, 8]
odd_numbers = [3, 5, 7, 9]

def square(x, y):
    return x **2, y **3

sqr_result = map(square, odd_numbers, even_number)

print(list(sqr_result))                      # op [(9, 8), (25, 64), (49, 216), (81, 343)]

