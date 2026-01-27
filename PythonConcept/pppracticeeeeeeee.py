data = [10, 10, 15, 15, 25, 33, 33, 42, 47, 51, 60, 60, 73, 88, 90, 99]


unique_items = set()  # 
duplicates = []       #10

for num in data:
    if num in unique_items:
        if num not in duplicates:
            duplicates.append(num)
    else:
        unique_items.add(num)

print(f"Duplicate values are: {duplicates}")