#         sets

myset1 = {1, 2, 3, 4, 4}
print(myset1)                          # op: {1, 2, 3, 4}

myset2 = {1,2,2,3,3,4,5}
print(myset2)                         # op: {1, 2, 3, 4, 5}

myset3 = (1,2,80,5, "ram",5, "sham")
print(myset3)                         # (1, 2, 80, 5, 'ram', 5, 'sham')
print("============")

# Accessing the items/ value from the set

'''as indexing is not followed by set we can't access by using indexing
but we can access by using for Loop and specifed items by using in keyword'''

for i in myset3:
    print(i)
print("================")

print("ram" in myset3)              # op: True
print("ram" in myset2)              # op: False
print("========")

# finding the lenth of set  : we use len() function
print(len(myset3))                 # op: 7
print("======")

# add items in the set

my_set = {1, 2, 3}
my_set.add(4)            # Adds a single element
my_set.update([5, 6])    # Adds multiple elements  or add multiple sets
print(my_set)            # Outputs: {1, 2, 3, 4, 5, 6}

myset1.update(myset2)
print(myset1)             # {1, 2, 3, 4, 5}

# Removing the items from the set by using following methods

myset1.remove(5)
print(myset1)                #op:  {1, 2, 3, 4, 5}
# myset1.remove(100)           # op: KeyError: 100  because 100 not present in set
# print(myset1)
print("=========")

myset1.discard(400)           # this method does not throw error if the values are not present is set
print(myset1)               # op: {1, 2, 3, 4}

myset1.discard(4)               # op: {1, 2, 3}
print(myset1)
print("========")

myset1.clear()
print(myset1)                  # op set()

del myset1
# print(myset1)                   # op: NameError: name 'myset1' is not defined, Because after delete this is not exists
print("================")

# join two sets

# union() method and update() method, update we have above

myset1 = {"a", "b", "c", 1, 2}
myset2 = {1,2,3, "a"}

myset3 = myset1.union(myset2)
print(myset3)                            # op; {'b', 2, 1, 'c', 3, 'a'}


