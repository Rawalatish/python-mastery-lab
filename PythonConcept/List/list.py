
mylist1 = [1, 20, 30, 5, 60]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = ["ram", "sham", "100", "200"]
mylist4 = list()   # empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)
print("=============")

# Accessing the items from the list

print(mylist2[1])                 # op: banana
print(mylist2[-1])                 # op: cherry
print(mylist2[-2])                 # op: banana
print("=============")

# Accessing items from list with range of index

print(mylist3[0 : 3])            # op: ['ram', 'sham', '100']
print(mylist3[1:3])              # op: ['sham', '100']
print(mylist3[2:0])              # op: []
print(mylist3[0:-1])             # op: ['ram', 'sham', '100']  end point mai se by default -1 ho jata hai so here -1-1 = -2
print(mylist3[-3:-1])            # op: ['sham', '100']

print("=============")

# Accessing all items from list by using for Loop:

for i in mylist3:
    print(i)