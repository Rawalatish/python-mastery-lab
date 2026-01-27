# integer numbers
# float numbers


x = 10
y = -2020202
z = 3.143

print(type(x))
print(type(z))

# number type conversion or type casting

p = float(x)
print(p)                   # op: 10.0
print(type(p))             # op: float

q = int(z)
print(q)                   # op : 3
print(type(q))

# max function

a = 10, 20, 30, 40, 25, 22, 62
print("this is the maximum value of a ", max(a))

# min function
print("this is the minimum value of a ", min(a))

#  random method
import random

print(random.random())    # return random value bet 0 to 1

# randint method
print(random.randint(2,10))     # op: any random value between 2 to 10
