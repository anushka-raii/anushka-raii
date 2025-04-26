seats = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0]
]

for row in seats:
    for seat in row:
        if seat == 1:
            print('B', end=' ')
        else:
            print('A', end=' ')
    print()
