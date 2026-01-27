import keyword

print(keyword.kwlist)

'''
 op: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
   'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
a= 10
b = 20

# as = 30  This is key word so we are not able to assign the to this

print(" How to check given word is keyword or not is following")

print(keyword.iskeyword("sss") ) # This will return True if the String is keyword otherwise False

print((keyword.iskeyword("finally")))  # This will return True if the String is keyword otherwise False
