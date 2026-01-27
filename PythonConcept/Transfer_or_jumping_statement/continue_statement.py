for i in range(10):
    if i == 5:
        continue
    print(i, end= " ")        # op: 0 1 2 3 4 6 7 8 9  here 5 is not printed because we use continue

print(" ============ ")

for number in range(5):
    if number == 2:
        continue  # Skip the rest of the loop when number is 2
    # print(number)
    print(number)         # op: 0 1 3 4

#    Using with a While Loop:

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing when count is 3
    print("Count is:", count)    # op : count is 1, 2, 4. 5

#         Combining with Conditions

for number in range(10):
    if number % 2 == 0:                  # == 1 for print odd number
        continue  # Skip even numbers
    print(number)  # Print odd numbers 