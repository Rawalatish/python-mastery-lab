# Membership Operators

a = " welcome to the python community"
b = "welcome"
c = "java"

print(b in a)        # op: True  - because b = welcome is present in the a=  value
print(b not in a)    # op: False
print(c in a)        # op: False

d = ["apple", "banana", "orange"]
e = "orange"
f = "mango"

print(e in d)        # True
print(e not in d)    # False
print(f in d)
print(f not in d)