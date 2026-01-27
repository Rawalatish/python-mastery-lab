# Dictionaries

mydict1 = {"brand": "ford", "model":"range", "year": 1820}

print(mydict1)                           # op: {'brand': 'ford', 'model': 'range', 'year': 1820}

print(mydict1["model"])
print("=====")


mydict1 = {"brand": "ford", "model":"range", "year": 1820, "year": 1900}
print(mydict1)                           # {'brand': 'ford', 'model': 'range', 'year': 1900}

# Finding the length of dictionary

print(len(mydict1))                        # op : 3

# data types

mydict2 = {"brand": "ford", "model":"range", "year": 1820, "10": 12.35, "buy": True}
print(mydict2)                        # op: {'brand': 'ford', 'model': 'range', 'year': 1820, '10': 12.35, 'buy': True}

# Accessing the items
print(mydict2["year"])              #op: 1820

# by get method
print(mydict2.get("model"))         # op: range

# by keys() method : it will access all keys and return in list of all keys
print(mydict2.keys())               # op: dict_keys(['brand', 'model', 'year', '10', 'buy'])

# by values() method : it will access all pairs and return in list of all pairs
print(mydict2.values())           # op: dict_values(['ford', 'range', 1820, 12.35, True])
print("=========")

# items() method, it will access all key and value in the form as tuple in a list
print(mydict2.items())        # op:dict_items([('brand', 'ford'), ('model', 'range'), ('year', 1820), ('10', 12.35), ('buy', True)])

# To determine the if a specified key is present in a dictionary use in keyword

if "year" in mydict2:
    print("yes, defined key is present in mydict")   #op: yes, defined key is present in mydict

# To change the value of specific item by referring to its key name
mydict2["year"] = 2002
print(mydict2)               # op: {'brand': 'ford', 'model': 'range', 'year': 2002, '10': 12.35, 'buy': True}

# Update dictionary
mydict2.update({'year':2021})
print(mydict2)               # op: {'brand': 'ford', 'model': 'range', 'year': 2021, '10': 12.35, 'buy': True}

mydict2.update({"mode":"on"})
print(mydict2)              # op: {'brand': 'ford', 'model': 'range', 'year': 2021, '10': 12.35, 'buy': True, 'mode': 'on'}

# Remove items:  pop() method is used
mydict2.pop("model")
print("by pop method", mydict2)             # op: {'brand': 'ford', 'year': 2021, '10': 12.35, 'buy': True}

''' popitem() method it will remove last last items'''
mydict2.popitem()
print(mydict2)             # op: {'brand': 'ford', 'model': 'range', 'year': 2021, '10': 12.35}

'''del keyword - it will delete specified key name'''
del mydict2["model"]
print(mydict2)             # op: {'brand': 'ford', 'year': 2021, '10': 12.35}

# del mydict2
# print(mydict2)           # op: error throws : NameError: name 'mydict2' is not defined. Did you mean: 'mydict1'?


# clear() method - it will remove all items and empties the dict
mydict2.clear()
print(mydict2)             # op: {}

# copy() method:
mydict2 = {"brand": "ford", "model":"range", "year": 1820, "10": 12.35, "buy": True}
newdict = mydict2.copy()
print(newdict)               #op: {'brand': 'ford', 'model': 'range', 'year': 1820, '10': 12.35, 'buy': True}
''' or we can also use dict() function for copy '''
newdict = dict(mydict2)
print(newdict)              # op: {'brand': 'ford', 'model': 'range', 'year': 1820, '10': 12.35, 'buy': True}

# Loop through Dictionary
for i in mydict2:
    print(i)              # op: brand model year 10 buy all this print in individual line

''' to print all values name'''
for i in mydict2:
    print(mydict2[i])       # op: all values name will be print in individual line


