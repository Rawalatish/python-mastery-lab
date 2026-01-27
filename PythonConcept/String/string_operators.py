# slicing operator

# syntax : str[strat : end]

name = "waterfall"

print(name[0:5])     # op: water   => indexing
print(name[:5])      # op: water   => by default start from 0 indexing if start value is not given
print(name[4:])      # op: rfall   => by default up to last indexing if end value is not given not giving

print(name[4:5])     # op: r  => end value indexing is excluded

print(name[3:-1])    # op: erfal   => - means from the reverse
print(name[0:5])


# ord() and chr() function

print(ord("a"))    # op: 97
print(ord("A"))    # op: 65

print(chr(97))     # op: a
print("========")

# len(), max() and min() function

print(len("python"))      # op: 6
print(max("abcd"))        # op: a
print(min("abcd"))        # op: d
print(max("python"))      # op: y
print("==========")

# in and not in operators

place = 'waterfallstation'

print('water'in place)        # op: True
print('abcd'in place)         # op: False

print('water'not in place)    # op: False
print('abcd'not in place)     # op: True
print("=========")

# Iterating string using for loop

place = "waterfall"

for i in place:
    print(i)

