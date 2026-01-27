# Logical operators

# and operators : It will return True only when both the statements are True otherwise false

a = 10
b = 20
c = 30

print((a < b) and (a < c))    # op: True
print((a < b) and (a > c))    # op: False


# or operator: It will return true if one of statement is true

print((a < b) or (a > c))    # op: True

# not operator : It will reverse the result

print(not (a < b))    # op: False   if True