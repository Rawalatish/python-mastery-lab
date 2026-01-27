a = 20
b = 20
c = 30

print(id(a))   # op: 140736535350296
print(id(b))   # op: 140736535350296    memory location is same for both. same identity for both because same value
print(id(c))   # op: 140736535350616

print(a is b)  # True
print(a is c)  # False
print(a is not c) # True

d = ["apple", "banana", "orange"]
e = ["apple", "banana", "orange"]

print(id(d))   # op: 1355774808448
print(id(e))   # op: 1355774810304  here both the identity is different for same values because we used list []

print(d == e)  # True   because its compare by values
print(d is e)  # False   it compare by id 
print(d is not e) # True
