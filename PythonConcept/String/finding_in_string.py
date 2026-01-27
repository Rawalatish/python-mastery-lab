'''
Finding in the string by using following methods
find()
rfind()
replace()
count()   all will be return -1 if the value is not found
'''

text = "Hello,welcome to the my world, welcome to Python."
index = text.find("welcome")
print(index)                     # Output: 6

print(text.find("java"))         # op: -1

print(text.rfind("welcome"))     # op: 31
print(text.rfind("magic"))       # op: -1

print(text.replace("welcome", "invited"))          #op: Hello,invited to the my world, invited to Python.
print(text.count("welcome"))     # op: 2