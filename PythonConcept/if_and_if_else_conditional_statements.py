# Conditional Statement => if | if - else | if - elif - else | nested if - else

#    if statement
a = 10

if a > 0:             # this is condition
    print("a is greater than 10")
print("it is outside of if block")

b = -20

if b > 0:             # this is condition
    print("b is greater than 10")
print("it is outside of if block")

print("===========================")
# if - else statement

# e = 50
e = 60

if e > 50:
    print(" if condition, it will print when the condition is true/matched")
else:
    print(" else condition, it will print when the condition is false/ dis-matched")

print("==============")

f = 10

if True:          # if we define True or 1 then it will take it as a True condition and if block only execute
    print(" if condition, it will print when the condition is true/matched")
else:
    print(" else condition, it will print when the condition is false/ dis-matched")

if False:         # if we define False or 0 then it will take it as a False condition and else block only execute
    print(" if condition, it will print when the condition is true/matched")
else:
    print(" else condition, it will print when the condition is false/ dis-matched")

print("=====================")

# Multiple statements in if-else in single line

print("python") if True else print("java")   # here True is condition if we define there any condition, depend on block exeute

f = 10
print("hi ") if f > 20 else print("bye")

g= 20
{print("hi "), print("fi")} if g > 20 else {print("bye"),print("statement 2 ")}



