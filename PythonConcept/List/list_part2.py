mylist = ["apple", "banana", "cherry"]
print(mylist)                   # op: ['apple', 'banana', 'cherry']

#  Changing the item values in the list

mylist[1] = "kiwi"
print(mylist)                   # op: ['apple', 'kiwi', 'cherry']
mylist[2] = "watermelon"
print(mylist)                   # op: ['apple', 'kiwi', 'watermelon']
print("============")

# Checking if item exist in list or not

mylist = ["apple", "banana", "cherry"]

if "apple" in mylist:
    print("apple is present in the list")
else:
    print("apple is not present in the list")
print("==========")

# Add items in the list

mylist.append("orange")                    # to add item to the end of list, use append() method
print(mylist)                              # op: ['apple', 'banana', 'cherry', 'orange']

mylist.insert(1, "mango")  # To add items at specific index position
print(mylist)                              # op: ['apple', 'mango', 'banana', 'cherry', 'orange']

# Remove items from the List
# pop() method:
mylist.pop(1)                              # to remove the specific items
print(mylist)                              # op: ['apple', 'banana', 'cherry', 'orange']

mylist.pop()                               # last index item will be removed if indexing is not defined in the pop() method
print(mylist)                              # op: ['apple', 'banana', 'cherry']
print("==========")
# del keyword

del mylist[1]
print(mylist)                              # op: ['apple', 'cherry']
print("--------")

# del mylist
# print(mylist)                              # op : NameError: name 'mylist' is not defined. Did you mean: 'list'?

# remove() method
mylist.remove("cherry")                    # remove defined item
print(mylist)                              # op: ['apple']

# clear method
mylist.clear()
print(mylist)                             # op : []

# copy() method

list1 = ["a", "b", "c", "d"]
list2 = list1.copy()
print(list2)                             # op: ['a', 'b', 'c', 'd']
print("========")

# Joining and combining the List

list3 = ["a", "b", "c", "d"]
list4 = [1, 2, 3, 4]
list5 = list3 + list4
print(list5)                            # op: ['a', 'b', 'c', 'd', 1, 2, 3, 4]
print("============")

'''another way to combine the list 
by using for loop'''


for i in list4:
    list3.append(i)
print(list3)                           # op: ['a', 'b', 'c', 'd', 1, 2, 3, 4]
print("============")

'''by using extend() function'''

list6 = [ "x", "y", "z"]
list7 =[10, 20 ,30]
list6.extend(list7)
print(list6)                          # op: ['x', 'y', 'z', 10, 20, 30]

# Sorting List : sort() method

# in ascending order
list8 = [ "ram", 'sham', "a", "d", "c"]
list9 = [1, 20, 333, 45, 5, ]

list8.sort()
print(list8)                        # op: ['a', 'c', 'd', 'ram', 'sham']

list9.sort()
print(list9)                        # op: [1, 5, 20, 45, 333]

# in descending order

list9.sort(reverse=True)
print(list9)                        # op: [333, 45, 20, 5, 1]
