# Using enumerate() function with list

fruits_list = ["apple", "mango", "banana", "cherry"]

fruit_enum = enumerate(fruits_list)

for index, fruit in fruit_enum:
    print(index, fruit)                       # op: a pair of index and value

# op :
# 0 apple
# 1 mango
# 2 banana
# 3 cherry