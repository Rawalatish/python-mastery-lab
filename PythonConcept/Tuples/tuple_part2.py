mytuple = ("apple", "banana", "kiwi")

# mytuple[1] = "lemon"

'''update the tuple by using list : tuple -> list (make changes here and again convert to tuple) ->'''
mylist = list(mytuple)
mylist[1] = "watermelon"
print(mylist)                             # ['apple', 'watermelon', 'kiwi']
mytuple = tuple(mylist)
print(mytuple)                            # ('apple', 'watermelon', 'kiwi')

# tuple count() and index() method:

print(mytuple.count("apple"))              # op: 1

print(mytuple.index("kiwi"))               # op: 2
print("==========")

# Unpacking tuples

mytuple =  ("apple", "banana", "kiwi")             # packing

(green, yellow, red) = mytuple
print(green)                                    # op: apple
print(yellow)                                   # op: banana
print(red)                                      # op: kiwi

mytuple1 =  ("apple", "banana", "kiwi", "lemon", "orange")

(a, b, *c) = mytuple1
print(a)                    # op: apple
print(c)                   # op: ['kiwi', 'lemon', 'orange']
print("============")

(a, *b, c) = mytuple1

print(a)                    # op: apple
print(b)                    # op: ['banana', 'kiwi', 'lemon']
print(c)                   # op: orange


