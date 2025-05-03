#Write a function find_maximum(a, b, c) that takes three numbers as parameters and returns the largest among them.
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Maximum is:", find_maximum(10, 30, 20))  # Output: 30
