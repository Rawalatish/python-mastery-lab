user_data = {"name": "Alice", "age": 25, "city": "New York"}

# Check if the value 25 exists in the dictionary
if 25 in user_data.values():
    print("Value found!")
else:
    print("Value not present.")

# Check if the key city exists in the dictionary
if "city" in user_data.keys():
    print("Value found!")
else:
    print("Value not present.")

user_data.pop("city")
print(user_data)

user_data.update({"dist": "NSatara"})
print(user_data)

user_data.popitem()
print(user_data)

