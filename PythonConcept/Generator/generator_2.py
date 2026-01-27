


def countdown(n):
    while n > 0:
        yield n                # this is generator
        n = n - 1              # exit condition

# creating object of generator
# use the generator

my_generator_obj = countdown(5)

# Iterating By using next() method : getting values one by one
#
# print(next(my_generator_obj))           # op: 5
# print(next(my_generator_obj))           # op: 4
# print(next(my_generator_obj))           # op: 3
# print(next(my_generator_obj))           # op: 2
# print(next(my_generator_obj))           # op: 1

''' if we call/ print the, then it will throws error, because n = 5  and we called it 5 times'''

print(" **************** ")

# Iterate over the all values by using for_in loop

for num in my_generator_obj:
    print(num)