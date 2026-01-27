# nested if else statement

# if condition1:
#     # Code to execute if condition1 is true
#     if condition2:
#         # Code to execute if condition2 is also true
#     else:
#         # Code to execute if condition1 is true but condition2 is false
# else:
#     # Code to execute if condition1 is false

a = 20

if a > 0:
    print(" a is positive number")
    if a > 20:
        print(" a is greater than 20")
    else:
        print(" a is less than 20")
elif a == 0:
    print(" a is 0")
else:
    print(" a is negative number")

print(" ==========")

experience = 5  # years of experience
education = "master's degree"  # level of education

if experience > 3:
    print("You have enough experience for senior positions.")

    if education == "master's degree":
        print("You are eligible for management roles.")
    elif education == "bachelor's degree":
        print("You can aim for mid-level roles.")
    else:
        print("Consider further education for better opportunities.")
else:
    print("You may want to gain more experience.")