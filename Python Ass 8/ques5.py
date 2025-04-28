#:Dictionary Key Reverser

data = {"one": 1, "two": 2, "three": 3}

reversed_data = {}
for key in data:
    value = data[key]
    reversed_data[value] = key

print(reversed_data)
