# Using enumerate function() with String

mystring = "hello"

mystring_enum = enumerate(mystring, start=0)  # we can start = 0 or 1, 2 , 3 , 4

for index, char in mystring_enum:
    print(index, char)


print(list(mystring_enum))

# op:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o