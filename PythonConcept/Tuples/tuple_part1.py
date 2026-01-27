# Empty tuple
empty_tuple = ()

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3])

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))

# One-element tuple (must include a comma)
single_element_tuple = (42,)

mytuple1 = (100, 200, 400)
mytuple2 = ("bat", "ball", "stumps")
mytuple3 = (1, "bat", "ball",2,  "stumps", 3)
print(mytuple2)
print("==========")

# Access the items from tuple

print(mytuple3[2])                        # op: ball
print(mytuple3[-2])                       # op: stumps

print(mixed_tuple[-2])           # op: 3.14
print(mixed_tuple[3])            # op: [1, 2, 3]
print(mixed_tuple[-1])            # op: [1, 2, 3]

print(mytuple3[-1])              # op: 3
print("==========")

# access the items from tuple with range of indexes:

mytuple4 = ('a', 'b', 'c', 'd', '1', '2', '3', '4')

print(mytuple4[2 : 4])                 # op: ('c', 'd')    in range index last range index get -1 by default in defined last range
print(mytuple4[2 : -2])                # op: ('c', 'd', '1', '2')      -2-1 = -3
print(mytuple4[2: ])                   # op: ('c', 'd', '1', '2', '3', '4')

# Access all items from tuple with for Loop

for i in mytuple4:
    print(i)

# check specific items exists in the tuple

if "b" in mytuple4:
    print("a is present in the tuple")
else:
    print("it does not exists")

# join tuples

mytuple5 = mytuple1 + mytuple2
print(mytuple5)                             # op: (100, 200, 400, 'bat', 'ball', 'stumps')
print("===========")

# multiply tuple : * operator used

fruits = ("mango", "cherry", "banana")
fruitstuple = fruits*2
print(fruitstuple)                          # op; ('mango', 'cherry', 'banana', 'mango', 'cherry', 'banana')
