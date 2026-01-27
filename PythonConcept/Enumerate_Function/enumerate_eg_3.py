# Converting enumerate function() to a list

mystring = "hello"

mystring_enum = enumerate(mystring, start=0)  # we can start = 0 or 1, 2 , 3 , 4

print(list(mystring_enum))