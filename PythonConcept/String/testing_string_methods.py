'''
isalnum()  Returns True if all char. in strings are alphanumeric
isalpha()  same for as above with method change
isdigit()
islower()
isupper()
isspace()
istitle() Reture True if the string follows the rule of title    => first letter of word must in upper case
'''

print("asdsdfg123".isalnum())    # op: True
print("asdsdfg123&&@".isalnum())    # op: False

print("Hi, My Name Is Python".istitle())  # True
print("Hi, My name Is Python".istitle())  # False

print("================")

'''
few more string methods
stratswith()
endswith()
lower()
upper()
title()
capitalize()
note: all string methods reture new values. They do not chnage the original values   
'''
text = "Hello,welcome to the my world, welcome to Python"

print(text.startswith("Hello"))            # op: True
print(text.startswith("to"))               # op: False

print(text.endswith("Python"))             # op: True
print(text.endswith("python"))             # op: False
print(text.lower())                        # op: hello,welcome to the my world, welcome to python
print(text.upper())                        # op: HELLO,WELCOME TO THE MY WORLD, WELCOME TO PYTHON
print(text.title())                        # op: Hello,Welcome To The My World, Welcome To Python
print(text.capitalize())                   # op; Hello,welcome to the my world, welcome to python
