marks = [
    [67, 78, 90],
    [56, 88, 92],
    [77, 76, 80],
    [90, 91, 85]
]

i = 0
while i < len(marks):
    total = 0
    j = 0
    while j < len(marks[i]):
        total += marks[i][j]
        j += 1
    print(f"Student {i + 1}: Total = {total}")
    i += 1
