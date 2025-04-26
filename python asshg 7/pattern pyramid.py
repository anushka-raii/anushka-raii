n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    stars = '* ' * i
    print(stars.center(n * 2))
